import anndata as ad
import scanpy as sc
import argparse
import numpy as np
import os
from cell_eval.utils import guess_is_lognorm

data_path = "datasets/obesity_challenge_1_local_gtruth.h5ad"
datadir = "datasets/"

print(f"Loading data from {data_path}...")
adata = ad.read_h5ad(data_path)

# Create train/test split
# We want about 50 cells of each perturbed gene in the test set
test_indices = []
np.random.seed(42)  # For reproducibility

unique_genes = adata.obs['gene'].unique()
print(f"Found {len(unique_genes)} unique genes.")

for gene in unique_genes:
    # Skip 'NC' (Non-Control) if we strictly interpret "perturbed", 
    # but typically we want controls in the test set too. 
    # We'll include 50 of each unique gene label found.
    
    gene_indices = np.where(adata.obs['gene'] == gene)[0]
    n_cells = len(gene_indices)
    
    if n_cells >= 50:
        selected_indices = np.random.choice(gene_indices, 50, replace=False)
    else:
        selected_indices = gene_indices
        
    test_indices.extend(selected_indices)

test_indices = np.array(test_indices)
test_mask = np.zeros(adata.n_obs, dtype=bool)
test_mask[test_indices] = True

adata_test = adata[~test_mask].copy()
adata_train = adata[test_mask].copy()

print(f"Train set size: {adata_test.n_obs}")
print(f"Test set size: {adata_train.n_obs}")

test_path = os.path.join(datadir, "test.h5ad")
train_path = os.path.join(datadir, "train.h5ad")

print(f"Saving test set to {test_path}...")
adata_test.write(test_path)

print(f"Saving train set to {train_path}...")
adata_train.write(train_path)

print("Done.")
