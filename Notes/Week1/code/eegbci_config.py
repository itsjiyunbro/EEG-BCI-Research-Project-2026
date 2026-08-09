from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = PROJECT_ROOT / "Datasets" / "raw"

SUBJECT_ID = 1 # first participant of this dataset
RUN_ID = 6 # 6th run of the record

PLOT_DURATION_SECONDS = 10
PLOT_CHANNEL_COUNT = 10