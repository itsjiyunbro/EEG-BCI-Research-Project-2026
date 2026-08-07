# Day 1 - MNE-Python Setup

> **Date:** 2026-08-08  
> **Study Time:** 2 h  
> **Project:** EEG & BCI Research Project  
> **Week:** Week 1 
> **Progress:** 4%

---

## Today's Goals

- [x] Goal 1
- [x] Goal 2
- [x] Goal 3

---

## Key Concepts

### 1. [MNE]

**One-sentence definition**

MNE is the analysis tool for EEG research

**Explanation**

- EEG file open
- watch Brain wave
- Denoising
- Observe Alpha wave, Beta wave, etc.
- Plot picture

**Why it matters for EEG/BCI research**
MNE is the crucial tool for EEG signal processing
It helps to interpret the EEG signal as I mentioned above.
---

### 2. [Info object]

**One-sentence definition**

> I created the *info* object

**Explanation**

- names of channels were ["Fz", "Cz", "Pz"]
- sampling frequency was 250.0 Hz
- type of channel was "eeg"

**Why it matters for EEG/BCI research**

It is the fundamental step for creating and analyzing eeg dataset.

---

## My Understanding

- create info by the function *mne.create_info*
- make continuous data by combining info with data by the function *mne.io.RawArray*

### Connection to Previous Knowledge

- eeg signal must be continuous, sequential data similar to audio signal, so it was not hard to understand the data type

---

## Code

### Key Code

```python
data = np.zeros((3, 250))
raw = mne.io.RawArray(data, info)
```

### Code Explanation

- **Purpose:**  import MNE, create "info" object
- **Input:**  `data` with shape `(3, 250)` and the `info` object
- **Output:**  A `RawArray` object containing three EEG channels and one second of data
- **Why it is used:**  MNE uses `Raw` objects to represent continuous EEG recordings

---

## Results

### Result 1 - Creating the Info Object

**Observation**

- created info by *mne.create_info* function
- created null signal data by *np.zeros*
- combined data with info by *mne.io.RawArray*

**Interpretation**

The result showed that EEG data needs both signal values and metadata. The `info` object describes the channels, while `RawArray` combines this information with continuous signal data.

---

## Insights / Ideas

- create information, and define channel names, sampling frequency, and dayta type by *mne.create_info*

---

## To Review

- [ ] *mne.create_info*
- [ ] *mne.io.RawArray*

---

## Questions

**Q. Why is the second dimension of `np.zeros((3, 250))` 250?**

A. It is the number of samples for one second of data because the sampling frequency is 250 Hz.

### Why?
It is the number of samples for one second of data because the sampling frequency is 250 Hz.

**Q. What is the role of '*mne.io.RawArray*'?**

A. combine data & info in the way of *mne.io.RawArray(data, info)*

---


**Problem:** PowerShell could not find `.venv\Scripts\python.exe`.

**Cause:** PowerShell was opened in `C:\Users\bjy99` instead of the project folder.

**Solution:** Moved to the project folder with `cd D:\EEG` before running the script.

**What I learned:** Relative paths such as `.\.venv` depend on the current working directory.

---

## References

- [MNE-Python Documentation](https://mne.tools/)

---

## Next Step

- [ ] import real eeg signal data
- [ ] see the eeg wave in my eyes

---

## Summary


1. Imported MNE-Python
2. Created an `Info` object with three EEG channels and a 250 Hz sampling frequency
3. Created a one-second practice `RawArray` and learned that EEG data requires both signal values and metadata

---

## End-of-Day Check

- [x] Did I achieve today's goals?
- [x] Did I save figures or results?
- [x] Did I organize the key code in the `code/` folder?
- [x] Did I record unanswered questions?
- [ ] Did I create a Git commit?

**Today's Commit Message**

```text
docs: complete Day 1 research note
```