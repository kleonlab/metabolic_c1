import anndata as ad
import scanpy as sc
import numpy as np
import os

testdatapath = "datasets/test.h5ad"
control_testdatapath = "datasets/control_test.h5ad"

print(f"Loading test data from {testdatapath}...")
adata = ad.read_h5ad(testdatapath)

# Identify control cells (assuming 'NC' is the control label)
control_label = 'NC'
control_mask = adata.obs['gene'] == control_label
control_cells = adata[control_mask]

print(f"Found {control_cells.n_obs} control cells out of {adata.n_obs} total cells")

if control_cells.n_obs == 0:
    raise ValueError(f"No control cells found with label '{control_label}'")

# Create a copy of adata
control_adata = adata.copy()

# Sample control cell expressions to match each cell
# For each cell, randomly sample a control cell's expression
np.random.seed(42)
control_indices = np.random.choice(control_cells.n_obs, size=adata.n_obs, replace=True)

# Get control X values
control_X = control_cells.X[control_indices]
if hasattr(control_X, "toarray"):
    control_X = control_X.toarray()

# Replace X with sampled control expressions
control_adata.X = control_X

# Also replace X_hvg in obsm if it exists
if 'X_hvg' in adata.obsm:
    control_hvg = control_cells.obsm['X_hvg'][control_indices]
    if hasattr(control_hvg, "toarray"):
        control_hvg = control_hvg.toarray()
    control_adata.obsm['X_hvg'] = control_hvg
    print(f"Also replaced .obsm['X_hvg'] with control expressions")

# The perturbation labels (gene column) remain unchanged
print(f"Perturbation labels preserved. Unique labels: {control_adata.obs['gene'].unique().tolist()}")

print(f"Saving control adata to {control_testdatapath}...")
control_adata.write(control_testdatapath)

print("Done.")
