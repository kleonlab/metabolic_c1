import anndata as ad
import scanpy as sc

data_path = "datasets/obesity_challenge_1_local_gtruth.h5ad"
print(f"Loading data from {data_path}...")
adata = ad.read_h5ad(data_path, backed='r') # Use backed mode to save memory

print("Columns in .obs:")
print(adata.obs.columns.tolist())

