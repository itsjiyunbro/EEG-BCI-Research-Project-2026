from eegbci_io import load_eegbci_raw
import matplotlib.pyplot as plt
import mne
import numpy as np

raw = load_eegbci_raw(preload=True)
"""
raw.plot(
    start = 0,
    duration = 10,
    n_channels = 10,
    scalings = {"eeg": 100e-6},
    title = "Raw EEG for Artifact Inspection",
    block = True,
)
"""

#print(raw.annotations.to_data_frame())
#print(raw.annotations)

spectrum = raw.compute_psd(
    fmin = 1.0,
    fmax = 80.0,
)
"""
spectrum.plot(
    picks="eeg",
    average = True,
)
plt.show(block = True)
"""

### 60 Hz POWER-LINE NOISE ###
raw_notched = raw.copy()

# Applying Notch Filter
raw_notched.notch_filter(
    freqs=[60.0],
)

notched_spectrum = raw_notched.compute_psd(
    fmin = 0.0,
    fmax = 80.0,
)
"""
notched_spectrum.plot(
    picks = "eeg",
    average = True,
)
plt.show(block = True)
"""

### ELECTRODE ARTIFACT ###
peak_annotations, bad_channels =  mne.preprocessing.annotate_amplitude(
    raw_notched,
    peak = 150e-6,
    picks="eeg",
)

print(peak_annotations)
print("Detected bad channels:", bad_channels)
print(peak_annotations.to_data_frame())

# Find sample changes over 150 µV
eeg_data = raw_notched.get_data(picks="eeg")
sample_differences = np.abs(np.diff(eeg_data, axis=1))

channel_indices, sample_indices = np.where(sample_differences >= 150e-6) # above 150 µV

for channel_index, sample_index in zip(channel_indices, sample_indices):
    channel_name = raw_notched.ch_names[channel_index]
    onset_seconds = sample_index / raw_notched.info["sfreq"]

    print(
        f"Channel: {channel_name}"
        f"onset: {onset_seconds:.5f} s"
    )

raw_notched.plot(
    start = 38.5,
    duration = 2.0,
    picks = ["Fp1", "Fpz", "Fp2", "AF7", "AF3", "C3", "Cz", "C4", "O1", "Oz", "O2"],
    scalings = {"eeg": 100e-6},
    title = "Amplitude candidate around 39.14s",
    block = True,
)


# Global Transient Candidate
global_transient_onset = 39.14375
global_transient_duration = 0.01250

raw_with_candidate = raw_notched.copy()

raw_with_candidate.annotations.append(
    onset = [global_transient_onset],
    duration = [global_transient_duration],
    description = "global_transient_candidate",
)

print(raw_with_candidate.annotations)


### MUSCLE ARTIFACT ###
muscle_annotations, muscle_scores = mne.preprocessing.annotate_muscle_zscore(
    raw_notched,
    threshold = 4,
    ch_type = "eeg",
    filter_freq = (30,70)
)
"""
print(muscle_annotations)

# Plot muscle score graph
plt.figure(figsize=(12,4))

plt.plot(raw_notched.times, muscle_scores)
plt.axhline(y=4, color="red", linestyle="--", label="Threshold = 4")

plt.xlabel("Time (s)")
plt.ylabel("Muscle z-score")
plt.title("Muscle Artifact Candidate Scores")
plt.legend()

plt.show(block = True)
"""


### EYE-MOVEMENT ARTIFACT ###
# ICA Preparation
raw_ica = raw_notched.copy()

raw_ica.annotations.append(
    onset = [global_transient_onset],
    duration = [global_transient_duration],
    description = ["BAD_global_transient"],
)

raw_ica.filter(
    l_freq = 1.0,
    h_freq = None,
)

# Create & Train ica
ica = mne.preprocessing.ICA(
    method="fastica",
    random_state = 97,
    max_iter = "auto",
)

ica.fit(
    raw_ica,
    picks="eeg",
    reject_by_annotation = True,
)
print(ica)

component_figures = ica.plot_components(
    picks = range(20),
    show=False,
)
"""
component_figures.savefig(
    "Notes/Week1/images/day5_ica_component_00_19.png",
    dpi=200,
    bbox_inches="tight",
)
plt.show(block=True)
"""
# Plot ICA000

ica.plot_sources( # time-domain relative waves
    raw_ica,
    picks = [0],
    start = 0,
    stop = 20,
    block = True,
)
ica.plot_properties( # property w/ PSD
    raw_ica,
    picks = [0],
    dB=True,
    reject_by_annotation = True,
)
#plt.show(block = True)

#
eog_indices, eog_scores = ica.find_bads_eog(
    raw_ica,
    ch_name = "Fpz",
    threshold = 3.0,
)
print("EOG-like ICA components: ", eog_indices)
print("EOG correlation scores: ", eog_scores)