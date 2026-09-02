## Goal: Subject 1의 Run 4를 열어서 구조를 확인한다.

import mne
from mne.datasets import eegbci

# Subject 1, Run 4
subject = 1
run = [4]

# Download EEGBCI data
raw_fnames = eegbci.load_data(subject, run)

print(raw_fnames)

raw = mne.io.read_raw_edf(raw_fnames[0], preload=True)

print(raw)

print("Number of channels:", raw.info["nchan"])
print("Sampling frequency:", raw.info["sfreq"])
print("Number of time samples:", raw.n_times)
print("Duration (sec):", raw.times[-1])

print("\nData Shape:")
print(raw.get_data().shape)

print("\nChannel names:")
print(raw.ch_names)

raw.plot(
    duration = 30,
    n_channels = 20,
    scalings = "auto",
    block = True,
)

# EEGBCI channel names alignment
eegbci.standardize(raw)

# Convert annotations to events
events, event_id = mne.events_from_annotations(raw)

print("\nEvent ID:")
print(event_id)

print("\nEvent shape:")
print(events.shape)

print("\nFirst 10 events:")
print(events[:10])