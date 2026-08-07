import mne
import numpy as np

ch = ["Fz", "Cz", "Pz"]

fs = 250

info = mne.create_info(
    ch_names = ch,
    sfreq = fs,
    ch_types = "eeg",
)

data = np.zeros((3, 250)) # 3개 EEG 채널에 대해, 각 채널당 250개의 0값 샘플로 된 연습용 신호 생성
raw = mne.io.RawArray(data, info) # 채널 정보(info)와 신호 데이터(data)를 결합 -> 연속 EEG 데이터 객체(RawArray) 생성


print(raw)