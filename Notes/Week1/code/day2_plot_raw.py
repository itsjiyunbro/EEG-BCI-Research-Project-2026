import mne

from eegbci_config import (
    PLOT_CHANNEL_COUNT,
    PLOT_DURATION_SECONDS,
    RUN_ID,
    SUBJECT_ID,
)

from eegbci_io import load_eegbci_raw

if __name__ == "__main__":
    raw = load_eegbci_raw(preload=False)

    print(raw)
    print("Number of channels: ", raw.info["nchan"])
    print("Sampling frequency: ", raw.info["sfreq"])
    print("Duration: ", raw.n_times / raw.info["sfreq"], "seconds")

    mne.viz.set_browser_backend("qt")

    raw.plot(
        duration = PLOT_DURATION_SECONDS,
        n_channels = PLOT_CHANNEL_COUNT,
        scalings = "auto",
        title = f"PhysioNet EEG - Subject {SUBJECT_ID}, Run {RUN_ID}",
        block = True,
    )