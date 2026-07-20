import os
import sys

def main():
    print("==========================================")
    print(" Kaggle ASL Alphabet Dataset Downloader ")
    print("==========================================\n")
    print("This script helps you download the ASL Alphabet dataset from Kaggle.")
    print("It requires the 'kaggle' Python package and a kaggle.json API token.\n")
    
    try:
        import kaggle
    except ImportError:
        print("Error: The 'kaggle' package is not installed.")
        print("Please install it by running: pip install kaggle")
        print("Note: Also make sure 'kaggle' is in your requirements.txt")
        sys.exit(1)
        
    print("Attempting to download 'grassknoted/asl-alphabet'...")
    try:
        kaggle.api.authenticate()
        print("Authentication successful. Downloading... (This may take a while, it is over 1GB)")
        kaggle.api.dataset_download_files('grassknoted/asl-alphabet', path='dataset/raw_kaggle', unzip=True)
        print("\nDownload and extraction complete!")
        print("Please move the class folders from 'dataset/raw_kaggle/asl_alphabet_train/asl_alphabet_train' into 'dataset/train/'")
        print("Then run 'python main.py' and press 't' to start preprocessing and training.")
    except Exception as e:
        print("\n[ERROR] Failed to download dataset.")
        print("Please make sure you have placed your kaggle.json file in the correct location:")
        print(" - Windows: C:\\Users\\<YourUsername>\\.kaggle\\kaggle.json")
        print(" - Mac/Linux: ~/.kaggle/kaggle.json")
        print(f"\nError Details: {e}")

if __name__ == "__main__":
    main()
