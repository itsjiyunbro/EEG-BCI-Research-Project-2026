# Day 1 — Understanding Motor Imagery EEG Data

> **Date:** 2026-09-02  
> **Study Time:** 1 h  
> **Project:** EEG & BCI Research Project  
> **Week:** Week 2 
> **Progress:** 17%

---

## Today's Goals

- [ ] Goal 1: Understand the structure of a real Motor Imagery EEG dataset before building an EEG classifier

---

## Key Concepts

### 1. Motor Imagery (MI)

**One-sentence definition**

**Motor Imagery** means imagining movement without actually performing it

**Explanation**

- Even without physical movement, motor imagery changes EEG activity over the **sensorimotor cortex**
- Important electrodes around this region includeL C3, Cz, C4
- Motor Imagery BCI attempts to distinguish different imagined movements from these EEG patterns

---

### 2. Alpha rhythm vs. Mu rhythm

**One-sentence definition**

> Both Alpha and Mu rhythms can occpuy approximately the **8-13 Hz** frqeuncy range. However they are not identical concepts

**Explanation**

- Alpha rhythm
| Frequency: approximately 8-13 Hz
| Commonly associated with posterior regions
| Often prominent during relaxed, eyes-closed states

- Mu rhythm
| Frequency: approximately 8-13 Hz
| Associated with the sensorimotor cortex
| Important in movement and Motor Imagery

> 💡EEG rhythms are not identified only by frequency
> Their spatial location and functional context are also important

---

### 3. Continuous-Time EEG vs. Continuous EEG Recording

**One-sentence definition**

> These two uses of the word **continuous** must be distinguished

**Explanation**

- Signal-processing perspective
Before Sampling: `Continuous-time analog EEG signal`
After Sampling: `Discrete-time digital EEG signal`
Therefore: `Continuous-time signal -> Sampling -> Discrete-time Signal`

- EEG-analysis perspective
💡 In EEG analysis, a **continuous EEG recording** usually means that the recorded EEG has not yet been segmented into epochs
It can already be sampled and digital
Therfore: `Continuous EEG recording -> Epoching -> Epoched EEG data`

> 💡In MNE, `Raw` does NOT mean an analog continuous-time signal
> `mne.io.Raw` represents sampled EEG data that has not yet been divided into epochs

---

### 4. Trial, Epoch, and Batch

**Trial**
A trial refers to one experimental attempt

Example:
> The participant is instructed to imagine moveing the right hand

This is one experimental trial

**Epoch**
An epoch is a segment of EEG data extracted around an event or trial

A single epoch can have the structure: `channels x time samples`

Example:
> `64 x 640` means 64 EEG channels, 640 time samples
> if sfreq is 160 Hz, then it is 4 second duration

**Batch**
A batch is a machine-learning concept
Multiple trials/epochs can be grouped together and processed by a model at once

Example:
> `batch_size = 16` may produce `16 x 64 x 640`
> 16 = epochs/trials in the batch
> 64 = channels
> 640 = time samples

- Therfore: 1 Trial/Epoch is 1 ML example, and 1 Batch is multiple Trials/Epochs

---

### 5. Raw EEG Data Structure

> We loaded Subject 1, Run 4 using MNE

**Data Structure**
- Channels: **64**
- Sampling frequency: **160 Hz**
- Recording duration: approximately **125 seconds**
- Time samples: **20,000**

**Data Shape**
`(64, 20000)`
> This means: `(channels, time samples)`
> The number of samples is consistent with:
`160 samples/sec x 125 sec = 20,000 samples`

**2D matrix**
              Time samples →
        ┌───────────────────────┐
Ch 1    │ • • • • • • • • • • │
Ch 2    │ • • • • • • • • • • │
...     │                       │
Ch 64   │ • • • • • • • • • • │
        └───────────────────────┘

> At this stage, the data has **not yet been epoched**

---

### 6. Events

> MNE extracted events from the EEG annotations

**Event Array**
`events.shape = (30,3)`

> 30 events were detected
> Each event contains 3 values (T0, T1, T2)

**Event Structure**
`[starting sample index, previous value, event ID]`

- Event ID
`1 (T0)`: Rest
`2 (T1)`: Left-hand Motor Imagery
`3 (T2)`: Right-hand Motor Imagery

- For example
`[672, 0, 3]`

> the correspoing time is `672 / 160 = 4.2 seconds`
> At sample 672(4.2s), a T2/Right-hand MI event begins

---

### 7. Raw -> Events -> Epochs

- Day 1 (current state)
> Current phase: `Raw EEG -> Events identified`
> Current shape: `(channels, time sampels)`

- Day 2
> These events will be used to segment the continuous EEG recording
> `Raw EEG -> Events -> Epoching -> Multiple Epochs`
> Resulting data will have a 3D structure: `(epochs, channels, time samples)`
> This will eventually become the input data for our EEG classifier

---

## Code

### Key Code 1

```python
eegbci.standardize(raw)
```

- **Purpose:**  Align EEGBCI channel names (C3, Cz, C4, Fpz, ...)

### Key Code 2

```python
events, event_id = mne.events_from_annotations(raw)
```

- **Purpose:**  Convert annotations into events

---

## Results

### Result 1 — [Result Name]

![result](images/dayX_result1.png)

**Observation**

- 
- 
- 

**Interpretation**

> Explain what the result means, not only what it looks like.

---

## Idea

> Our planned Motor Imagery classification pipeline is:

`Raw EEG`
`↓`
`Preprocessing / Band-pass Filtering`
`↓`
`Epoching`
`↓`
`CSP (Common Spatial Pattern)`
`↓`
`Feature Extraction`
`↓`
`LDA (Linear Discriminant Analysis)`
`↓`
`Left-hand MI / Right-hand MI`

**Common Spacial Patter (CSP)** extracts spatial EEG patters that help distinguish the two Motor Imagery classes

Conceptually, it attempts to find spatial patterns that differ strongly between:
- Left-hand Motor Imagery
- Right-hand Motor Imagery

**Linear Discriminant Analysis (LSD)** uses the extracted features to perform the final classification
---

## Next Step

- [ ] Segment the EEG recording into epochs using MI events
- [ ] Examine the resulting `(epochs, channels, time samples)` structure
- [ ] Prepare the epochs for Motor Imagery classification

---

## Summary

1. Motor Imagery can be classified using changes in sensorimotor EEG activity, particularly mu and beta rhythms
2. MNE `Raw` represents a sampled continuous EEG recording, while events indicate when each experimental condition occurs
3. Subject 1 Run 4 contains 64 channels x 20,000 samples, with T1 and T2 representing Left- and Right-hand Motor Imagery

---

**Today's Commit Message**

```text
docs: complete Day 1 research note
```