# Day 6 — Epoch Creation and Inspection

> **Date:** 2026-08-25
> **Study Time:** 2 h  
> **Project:** EEG & BCI Research Project  
> **Week:** Week 1
> **Progress:** 15%

---

## Today's Goals

- [x] Goal 1: Convert T0, T1, and T2 annotations into events
- [x] Goal 2: Create 0-4s EEG epochs for each condition
- [x] Goal 3: Inspect the epoch structure and save the processed data

---

## Key Concepts

### 1. Sampling Frequency

**One-sentence definition**

The sampling frequency is **the number of samples** recorded **per second** (1초당 샘플 개수)

---

### 2. Conditions and Epochs

**One-sentence definition**

> There are 3 conditions: T0 (rest), T1 (motor imagery of opening and closing both fists), and T2 (motor imagery of opening and closing both feet)

**Explanation**

- T0 has 15 epochs
- T1 has 7 epochs 
- T2 has 8 epochs

---

### 3. Annotations and Events

**Explanation**

- Annotations: T0, T1, T2
- Events convert these annotation onsets into sample-based markers for each epoch creation
- The epoch data shape was '(30, 64, 641)': 30 epochs, 64 channels per epoch, and 641 samples per channel from 0 to 4 s at 160 Hz

---

## Code

### Key Code

```python
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
```

### Code Explanation

- **Purpose:** Create condition-specific EEG epochs from continuous Raw data using event onsets

---

### Key Code

```python
print("Data shape: ", epochs.get_data().shape)
```

### Code Explanation

- **Purpose:** Print the shape of the epoch data array

---

## Next Step

- [ ] Load the saved epochs for condition-based analysis 
- [ ] Compute PSD for T0, T1, and T2 epochs
- [ ] Compare alpha- and beta- band power at C3, Cz, and C4

---

## Summary

1. The sampling frequency of 160 Hz means that 160 EEG samples are recorded per second
2. T0, T1, and T2 annotations were converted into events, which defined the starting points of EEG epochs
3. A total of 30 epochs are created: 15 T0 epochs, 7 T1 epochs, 8 T2 epochs
4. Each epoch contained 64 EEG channels and 641 samples from 0 to 4 s
5. The epoched data were saved in FIF format for Day7 condition-based PSD analysis

---

**Today's Commit Message**

```text
docs: complete Day 6 research note
```