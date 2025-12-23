import requests
from tqdm.auto import tqdm  # picks the best bar for the environment
from pathlib import Path

# Find repository root by looking for pyproject.toml (or .git as fallback)
def find_repo_root():
    """Find the repository root directory."""
    current = Path(__file__).resolve().parent
    while current != current.parent:
        if (current / "pyproject.toml").exists() or (current / ".git").exists():
            return current
        current = current.parent
    # Fallback: if we reach filesystem root, use the script's parent's parent
    # (assuming script is in scripts/ directory)
    return Path(__file__).resolve().parent.parent

repo_root = find_repo_root()
url = "https://storage.googleapis.com/vcc_data_prod/datasets/state/competition_support_set.zip"
output_path = repo_root / "datasets" / "competition_support_set.zip"
extract_path = repo_root / "datasets" / "competition_support_set"

# stream the download so we can track progress
response = requests.get(url, stream=True)
total = int(response.headers.get("content-length", 0))

# Ensure datasets directory exists
output_path.parent.mkdir(parents=True, exist_ok=True)

with open(output_path, "wb") as f, tqdm(
    total=total, unit='B', unit_scale=True, desc="Downloading"
) as bar:
    for chunk in response.iter_content(chunk_size=8192):
        if not chunk:
            break
        f.write(chunk)
        bar.update(len(chunk))

# unzip the dataset
import zipfile
with zipfile.ZipFile(output_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

print(f"Dataset downloaded and extracted to {extract_path}")

# delete the zip file
output_path.unlink()
print(f"Zip file deleted")