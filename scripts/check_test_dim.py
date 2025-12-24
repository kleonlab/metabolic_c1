import anndata as ad
import numpy as np

data_path = "datasets/test.h5ad"
print(f"Loading data from {data_path}...")
adata = ad.read_h5ad(data_path)

if "X_hvg" in adata.obsm:
    print(f"X_hvg shape: {adata.obsm['X_hvg'].shape}")
else:
    print("X_hvg not found in .obsm")

print(f"n_vars: {adata.n_vars}")

