import anndata as ad
import scanpy as sc
import argparse
import numpy as np
import os
from cell_eval.utils import guess_is_lognorm

#data_path = "datasets/obesity_challenge_1_local_gtruth.h5ad"
data_path = "datasets/obesity_challenge_1.h5ad"
datadir = "datasets/"

print(f"Loading data from {data_path}...")
adata = ad.read_h5ad(data_path)

# Calculate Highly Variable Genes
print("Calculating highly variable genes...")
try:
    sc.pp.highly_variable_genes(adata, n_top_genes=2000, subset=False, flavor='seurat')
    # Use .highly_variable boolean mask to select genes
    hvg_mask = adata.var['highly_variable']
    adata.var['X_hvg'] = hvg_mask # Keep the boolean in var just in case
    
    # Store the actual expression matrix of HVGs in obsm['X_hvg']
    # If X is sparse, densify it for X_hvg if that's what the model expects, 
    # but check if it fits in memory.
    X_hvg = adata[:, hvg_mask].X
    if hasattr(X_hvg, "toarray"):
        X_hvg = X_hvg.toarray()
    adata.obsm['X_hvg'] = X_hvg
    
    print(f" identified {sum(hvg_mask)} highly variable genes and stored in .obsm['X_hvg']")
except Exception as e:
    print(f"Warning: Could not calculate HVGs: {e}")

# Add dummy columns for compatibility
if 'cell_type' not in adata.obs:
    print("Adding dummy 'cell_type' column...")
    adata.obs['cell_type'] = 'unknown'

if 'batch' not in adata.obs:
    print("Adding dummy 'batch' column...")
    adata.obs['batch'] = 'batch1'

# Ensure gene_name column exists in .var for compatibility
if 'gene_name' not in adata.var:
    print("Adding 'gene_name' column to .var from index...")
    adata.var['gene_name'] = adata.var.index

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
    
    if n_cells >= 100:
        selected_indices = np.random.choice(gene_indices, 100, replace=False)
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
