from pathlib import Path

import mne
from mne.datasets import eegbci

from eegbci_config import DATA_DIR, RUN_ID, SUBJECT_ID

def download_eegbci_run() -> Path:
    file_paths = eegbci.load_data(
        subjects = SUBJECT_ID,
        runs = [RUN_ID],
        path = DATA_DIR,
        update_path = False,
    )

    return Path(file_paths[0])

def load_eegbci_raw(preload: bool = False):
    edf_path = download_eegbci_run()
    raw = mne.io.read_raw_edf(edf_path, preload=preload)

    eegbci.standardize(raw) # set channel names
    montage = mne.channels.make_standard_montage("standard_1005")
    raw.set_montage(montage)

    return raw
