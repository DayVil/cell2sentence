import requests
import os
import gdown

SAVE_PATH = "tmp/saved/"
SAVE_NAME = "saved_data.h5ad"
DATA_PATH = os.path.join(SAVE_PATH, SAVE_NAME)

def download_data(url, name):
    output_dir = "tmp"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, name)
    
    # Skip download if file already exists
    if os.path.exists(output_path):
        print(f"File already exists at {output_path}, skipping download.")
        return output_path
    
    # Handle Google Drive URLs
    if "drive.google.com" in url:
        gdown.download(url, output_path, quiet=False, fuzzy=True)
    else:
        response = requests.get(url)
        response.raise_for_status()
        with open(output_path, 'wb') as file:
            file.write(response.content)
    
    return output_path

def save_data(adata):
    """
    Save AnnData object to the tmp/saved directory.
    
    Parameters
    ----------
    adata : anndata.AnnData
        The AnnData object to save
    name : str
        The filename for the saved data (should end with .h5ad)
    
    Returns
    -------
    str
        The full path where the data was saved
    """
    output_name = SAVE_NAME
    os.makedirs(SAVE_PATH, exist_ok=True)
    output_path = os.path.join(SAVE_PATH, output_name)
    
    adata.write_h5ad(output_path)
    
    return output_path