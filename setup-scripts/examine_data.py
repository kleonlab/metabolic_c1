import anndata as ad
import scanpy as sc
import argparse
import numpy as np
from cell_eval.utils import guess_is_lognorm



#data_path = "/home/b5cc/sanjukta.b5cc/metabolic_c1/datasets/obesity_challenge_1.h5ad"
#data_path = "/home/b5cc/sanjukta.b5cc/metabolic_c1/datasets/obesity_challenge_1_local_gtruth.h5ad"
data_path = "/home/b5cc/sanjukta.b5cc/metabolic_c1/datasets/test.h5ad"

print(f"Loading data from: {data_path}\n")
adata = ad.read_h5ad(data_path)
print(f"Observations: {adata.n_obs}")
print(f"Variables: {adata.n_vars}")
print(f"Is log-normalized: {guess_is_lognorm(adata)}")

print(adata.X[0])
print(adata.X[1:4][-35:])
# Print the first few rows of obs (cell/cell-annotation table)
print("\nFirst few rows of .obs (cell annotations):")
print(adata.obs.head())

gene_names = adata.obs['gene'].value_counts().index.to_list()
print(gene_names)
print(len(gene_names))
