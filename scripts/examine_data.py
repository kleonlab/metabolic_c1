import anndata as ad
import scanpy as sc
import argparse
import numpy as np
from cell_eval.utils import guess_is_lognorm


def print_dict_info(d, indent=2):
    """Print information about dictionary keys, their types and shapes."""
    prefix = " " * indent
    for key, value in d.items():
        if hasattr(value, 'shape'):
            print(f"{prefix}{key}: {type(value).__name__} with shape {value.shape}")
        elif hasattr(value, 'dtype'):
            print(f"{prefix}{key}: {type(value).__name__} with dtype {value.dtype}")
        elif isinstance(value, (list, tuple)):
            print(f"{prefix}{key}: {type(value).__name__} with length {len(value)}")
        elif isinstance(value, dict):
            print(f"{prefix}{key}: dict with {len(value)} keys")
        else:
            print(f"{prefix}{key}: {type(value).__name__}")


def examine_adata(adata_path):
    """Load and examine an AnnData object."""
    print(f"Loading data from: {adata_path}\n")
    adata = ad.read_h5ad(adata_path)
    
    # Basic shape information
    print("=" * 60)
    print("BASIC INFORMATION")
    print("=" * 60)
    print(f"Shape: {adata.shape} (n_obs × n_vars)")
    print(f"Observations: {adata.n_obs}")
    print(f"Variables: {adata.n_vars}")
    print(f"Is log-normalized: {guess_is_lognorm(adata)}")
    print()
    
    # Main data matrix
    print("=" * 60)
    print("MAIN DATA MATRIX (X)")
    print("=" * 60)
    if adata.X is not None:
        print(f"Type: {type(adata.X).__name__}")
        print(f"Shape: {adata.X.shape}")
        if hasattr(adata.X, 'dtype'):
            print(f"Dtype: {adata.X.dtype}")
    else:
        print("No main data matrix (X is None)")
    print()
    
    # Observations annotations
    print("=" * 60)
    print("OBSERVATIONS ANNOTATIONS (.obs)")
    print("=" * 60)
    if len(adata.obs.columns) > 0:
        print(f"Number of columns: {len(adata.obs.columns)}")
        for col in adata.obs.columns:
            dtype = adata.obs[col].dtype
            n_unique = adata.obs[col].nunique()
            print(f"  {col}: {dtype} ({n_unique} unique values)")
            
            # Special check for target_gene column
            if col == "target_gene" or col == "pert_name" or "pert" in col.lower():
                non_targeting_count = (adata.obs[col] == "non-targeting").sum()
                if non_targeting_count > 0:
                    print(f"    → Non-targeting cells: {non_targeting_count} ({non_targeting_count/len(adata.obs)*100:.2f}%)")
    else:
        print("No observation annotations")
    print()
    
    # Variables annotations
    print("=" * 60)
    print("VARIABLES ANNOTATIONS (.var)")
    print("=" * 60)
    if len(adata.var.columns) > 0:
        print(f"Number of columns: {len(adata.var.columns)}")
        for col in adata.var.columns:
            dtype = adata.var[col].dtype
            n_unique = adata.var[col].nunique()
            print(f"  {col}: {dtype} ({n_unique} unique values)")
    else:
        print("No variable annotations")
    print()
    
    # Unstructured annotations
    print("=" * 60)
    print("UNSTRUCTURED ANNOTATIONS (.uns)")
    print("=" * 60)
    if len(adata.uns) > 0:
        print(f"Number of keys: {len(adata.uns)}")
        print_dict_info(adata.uns)
    else:
        print("No unstructured annotations")
    print()
    
    # Observations multi-dimensional annotations
    print("=" * 60)
    print("OBSERVATIONS MULTI-DIMENSIONAL (.obsm)")
    print("=" * 60)
    if len(adata.obsm) > 0:
        print(f"Number of keys: {len(adata.obsm)}")
        print_dict_info(adata.obsm)
    else:
        print("No multi-dimensional observation annotations")
    print()
    
    # Variables multi-dimensional annotations
    print("=" * 60)
    print("VARIABLES MULTI-DIMENSIONAL (.varm)")
    print("=" * 60)
    if len(adata.varm) > 0:
        print(f"Number of keys: {len(adata.varm)}")
        print_dict_info(adata.varm)
    else:
        print("No multi-dimensional variable annotations")
    print()
    
    # Layers
    print("=" * 60)
    print("LAYERS (.layers)")
    print("=" * 60)
    if len(adata.layers) > 0:
        print(f"Number of layers: {len(adata.layers)}")
        print_dict_info(adata.layers)
    else:
        print("No layers")
    print()
    
    # Observations pairwise annotations
    print("=" * 60)
    print("OBSERVATIONS PAIRWISE (.obsp)")
    print("=" * 60)
    if len(adata.obsp) > 0:
        print(f"Number of keys: {len(adata.obsp)}")
        print_dict_info(adata.obsp)
    else:
        print("No pairwise observation annotations")
    print()
    
    # Variables pairwise annotations
    print("=" * 60)
    print("VARIABLES PAIRWISE (.varp)")
    print("=" * 60)
    if len(adata.varp) > 0:
        print(f"Number of keys: {len(adata.varp)}")
        print_dict_info(adata.varp)
    else:
        print("No pairwise variable annotations")
    print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Examine an AnnData (.h5ad) file structure")
    parser.add_argument("adata_path", type=str, help="Path to the AnnData .h5ad file")
    args = parser.parse_args()
    
    examine_adata(args.adata_path)