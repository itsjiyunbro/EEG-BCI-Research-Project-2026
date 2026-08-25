import mne

from eegbci_io import load_eegbci_raw

raw = load_eegbci_raw(preload = True)

event_id = {
    "T0": 1,
    "T1": 2,
    "T2": 3,
}

events, event_id = mne.events_from_annotations(
    raw,
    event_id = event_id,
)

print(events[:10])
print(event_id)

###
raw.filter(l_freq = 1.0, h_freq = 40.0)

epochs = mne.Epochs(
    raw,
    events,
    event_id = event_id,
    tmin = 0.0,
    tmax = 4.0,
    baseline = None,
    picks = "eeg",
    preload = True,
)

print(epochs)
print("Data shape: ", epochs.get_data().shape)

for condition in event_id:
    print(f"{condition} epochs: ", len(epochs[condition]))


###
t1_epochs = epochs["T1"]

print("T1 data shape: ", t1_epochs.get_data().shape)

t1_epochs.plot(
    n_epochs = 3,
    n_channels = 10,
    scalings = {"eeg": 100e-6},
    block = True,
)

epochs_path = "Datasets/processed/subject01_run06_1-40Hz-epo.fif"

epochs.save(
    epochs_path,
    overwrite = True,
)

print("Saved epochs to: ", epochs_path)


### Check T0, T1, T2 epoch in C3, Cz, C4 channels
central_channels = ["C3", "Cz", "C4"]

for conditions in event_id:
    epochs[conditions].plot(
        picks = central_channels,
        n_epochs = 3,
        n_channels = 3,
        scalings = {"eeg": 100e-6},
        block = True,
    )

saved_epochs = mne.read_epochs(
    "Datasets/processed/subject01_run06_1-40Hz-epo.fif",
    preload = True,
)

print(saved_epochs)
print("Reloaded data shape: ", saved_epochs.get_data().shape)