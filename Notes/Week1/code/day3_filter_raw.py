from eegbci_io import load_eegbci_raw

raw_original = load_eegbci_raw(preload=True)
raw_filtered = raw_original.copy() # copied EEG raw data

# Band Pass Filter
raw_filtered.filter(l_freq=1.0, h_freq=40.0) # filter() method: MNE의 Raw 객체에 주파수 필터를 적용

## Compare Original vs Filtered
raw_original.plot(
    start = 0,
    duration = 20,
    n_channels = 10,
    scalings={"eeg": 100e-6},
    title = "Original EEG",
    block = True,
)

raw_filtered.plot(
    start = 0,
    duration = 20,
    n_channels = 10,
    scalings={"eeg": 100e-6},
    title = "Filtered EEG (1-40 Hz)",
    block = True,
)

"""
start = 0: 기록의 0초부터 그리겠다.
duration = 10: 한 화면에 10초의 시간을 그리겠다.
n_channels = 10: 한 화면에 10개만 그리겠다. 나머지 채널은 스크롤해서 본다.
scalings = "auto": EEG 파형의 세로 크기를 자동으로 조정한다
blcok = True: 파형 창을 닫은 후에 Python program이 다음줄로 넘어가도록 한다.
"""