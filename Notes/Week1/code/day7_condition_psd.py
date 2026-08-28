import mne

epochs = mne.read_epochs(
    "Datasets/processed/subject01_run06_1-40Hz-epo.fif",
    preload = True,
)

print(epochs)

for condition in epochs.event_id:
    print(f"{condition} epochs: ", len(epochs[condition]))

# Compute PSD

central_channels = ["C3", "Cz", "C4"]

spectra = {}

for condition in epochs.event_id:
    spectra[condition] = epochs[condition].compute_psd(
        method = "welch",
        fmin = 1.0,
        fmax = 40.0,
        picks = central_channels,
        n_fft = 256,
    )

    print(
        f"{condition} PSD shape: ",
        spectra[condition].get_data().shape,
    )

### Compute mean PSD
mean_psd = {}

for condition in spectra:
    mean_psd[condition] = spectra[condition].get_data().mean(axis=0)

    print(
        f"{condition} mean PSD shape: ",
        mean_psd[condition].shape,
    )


### PLOT
import matplotlib.pyplot as plt
import numpy as np

frequencies = spectra["T0"].freqs

condition_colors = {
    "T0": "tab:blue",
    "T1": "tab:orange",
    "T2": "tab:green",
}

fig, axes = plt.subplots(
    nrows = 3,
    ncols = 1,
    figsize = (10,10),
    sharex = True,
)

for channel_index, channel_name in enumerate(central_channels):
    for condition in mean_psd:
        power_db = 10 * np.log10(
            mean_psd[condition][channel_index]
        )

        axes[channel_index].plot(
            frequencies,
            power_db,
            label = condition,
            color = condition_colors[condition],
        )
    axes[channel_index].set_title(channel_name)
    axes[channel_index].set_ylabel("PSD [dB]")
    axes[channel_index].legend()

axes[-1].set_xlabel("Frequency [Hz]")

fig.suptitle("Condition-wise PSD at Central EEG Channels")
fig.tight_layout()

fig.savefig(
    "Notes/Week1/images/day7_condition_psd_central_channels.png",
    dpi = 200,
    bbox_inches = "tight",
)

plt.show(block = True)


### Bands
bands = {
    "Alpha (8-13 Hz)": (8.0, 13.0),
    "Beta (13-30 Hz)": (13.0, 30.0),
}

band_power_db = {}

for condition in mean_psd:
    band_power_db[condition] = {}

    for band_name, (fmin, fmax) in bands.items():
        frequency_mask = (
            (frequencies >= fmin) & (frequencies <= fmax)
        )

        band_power = np.trapezoid(
            mean_psd[condition][:, frequency_mask],
            frequencies[frequency_mask],
            axis = 1,
        )

        band_power_db[condition][band_name] = (
            10 * np.log10(band_power)
        )

        for channel_name, power_db in zip(
            central_channels,
            band_power_db[condition][band_name],
        ):
            print(
                f"{condition} | {channel_name} | "
                f"{band_name}: {power_db: .2f} dB"
            )


fig, axes = plt.subplots(
    nrows = 1,
    ncols = 2,
    figsize = (12, 5),
    sharey = True,
)

x = np.arange(len(central_channels))
bar_width = 0.35

for axis, band_name in zip(axes, bands):
    t0_power = band_power_db["T0"][band_name]

    t1_change = band_power_db["T1"][band_name] - t0_power
    t2_change = band_power_db["T2"][band_name] - t0_power

    axis.bar(
        x - bar_width / 2,
        t1_change,
        width = bar_width,
        label = "T1 - T0",
        color = "tab:orange",
    )

    axis.bar(
        x + bar_width / 2,
        t2_change,
        width  = bar_width,
        label = "T2 - T0",
        color = "tab:green",
    )

    axis.axhline(
        y = 0,
        color = "black",
        linewidth = 1,
    )

    axis.set_title(band_name)
    axis.set_xticks(x)
    axis.set_xticklabels(central_channels)
    axis.set_xlabel("Channel")
    axis.legend()

axes[0].set_ylabel("Band-power difference from T0 [dB]")

fig.suptitle("Relative Central Band Power During Motor Imagery")
fig.tight_layout()

fig.savefig(
    "Notes/Week1/images/day7_relative_band_power.png",
    dpi = 200,
    bbox_inches = "tight",
)

plt.show(block = True)