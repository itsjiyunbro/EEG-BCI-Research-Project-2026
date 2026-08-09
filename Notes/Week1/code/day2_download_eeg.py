from eegbci_io import download_eegbci_run

if __name__ == "__main__":
    edf_path = download_eegbci_run()

    print("Downloaded file:")
    print(edf_path)
    
# raw.info["nchan"]: 64
# raw.info["sfreq"]: 160.0 Hz
# raw.n_times      : 20000 samples
# duration         : 125.0 seconds