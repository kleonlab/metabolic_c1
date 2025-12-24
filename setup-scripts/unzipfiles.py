
import zipfile
import os

def unzip_file(zip_path, extract_to):
    """
    Unzips a file to the specified directory.
    """
    print(f"Unzipping {zip_path} to {extract_to}...")
    
    # Check if file exists
    if not os.path.exists(zip_path):
        print(f"Error: File {zip_path} not found.")
        return

    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        print("Extraction complete.")
    except zipfile.BadZipFile:
        print("Error: The file is not a valid zip file.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage for your dataset
    dataset_dir = "datasets"
    zip_filename = "/home/b5cc/sanjukta.b5cc/metabolic_c1/datasets/obesity_challenge_1.h5ad.zip"
    
    zip_path = os.path.join(dataset_dir, zip_filename)
    extract_to = dataset_dir
    
    unzip_file(zip_path, extract_to)
