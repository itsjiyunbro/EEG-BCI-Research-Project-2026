import matplotlib.pyplot as plt
from eegbci_io import load_eegbci_raw

# Load EEG
raw = load_eegbci_raw(preload = True)
raw.filter(l_freq = 1.0, h_freq = 40.0)

# Compute PSD
spectrum = raw.compute_psd(fmin = 1.0, fmax = 40.0)

# Plot PSD
spectrum.plot(average=True, picks="eeg")
plt.show(block=True)

# Plot PSD of specified location
spectrum.plot(
    picks = ["C3", "Cz", "C4"],
    average = False,
    spatial_colors = True,
)
plt.show(block=True)

# 3 frequency bands to observe
bands = {
    "Theta (4-8 Hz)": (4,8),
    "Alpha (8-13 Hz)": (8,13),
    "Beta (13-30 Hz)": (13,30),
}

spectrum.plot_topomap(bands = bands, ch_type="eeg")
plt.show(block=True)