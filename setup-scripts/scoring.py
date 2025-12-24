import anndata as ad
import scanpy as sc
import argparse
import numpy as np

def get_mse_score(predfile_path, truthfile_path):
    pred_adata = ad.read_h5ad(predfile_path)
    print(f"Shape: {pred_adata.shape} (n_obs × n_vars)")
    print(f"Observations: {pred_adata.n_obs}")
    print(f"Variables: {pred_adata.n_vars}")

    truth_adata = ad.read_h5ad(truthfile_path)
    print(f"Shape: {truth_adata.shape} (n_obs × n_vars)")
    print(f"Observations: {truth_adata.n_obs}")
    print(f"Variables: {truth_adata.n_vars}")

    # Ensure shapes match
    if pred_adata.shape != truth_adata.shape:
        raise ValueError(f"Shape mismatch: {pred_adata.shape} vs {truth_adata.shape}")

    diff = pred_adata.obsm['X_hvg'] - truth_adata.obsm['X_hvg']

    
    # Handle sparse matrices
    if hasattr(diff, "toarray") or hasattr(diff, "todense"):
        mse_value = diff.power(2).mean()
    else:
        mse_value = np.mean(diff ** 2)

    return mse_value


def get_escore(predfile_path, truthfile_path):
    pred_adata = ad.read_h5ad(predfile_path)
    print(f"Shape: {pred_adata.shape} (n_obs × n_vars)")
    print(f"Observations: {pred_adata.n_obs}")
    print(f"Variables: {pred_adata.n_vars}")

    truth_adata = ad.read_h5ad(truthfile_path)
    print(f"Shape: {truth_adata.shape} (n_obs × n_vars)")
    print(f"Observations: {truth_adata.n_obs}")
    print(f"Variables: {truth_adata.n_vars}")

    # Ensure shapes match
    if pred_adata.shape != truth_adata.shape:
        raise ValueError(f"Shape mismatch: {pred_adata.shape} vs {truth_adata.shape}")

    diff = pred_adata.obsm['X_hvg'] - truth_adata.obsm['X_hvg']
    
    
    # Handle sparse matrices
    if hasattr(diff, "toarray") or hasattr(diff, "todense"):
        mse_value = diff.mean()
    else:
        mse_value = np.mean(diff)

    return mse_value

def get_pearson_score(predfile_path, truthfile_path):
    pred_adata = ad.read_h5ad(predfile_path)
    print(f"Shape: {pred_adata.shape} (n_obs × n_vars)")
    print(f"Observations: {pred_adata.n_obs}")
    print(f"Variables: {pred_adata.n_vars}")

    truth_adata = ad.read_h5ad(truthfile_path)
    print(f"Shape: {truth_adata.shape} (n_obs × n_vars)")
    print(f"Observations: {truth_adata.n_obs}")
    print(f"Variables: {truth_adata.n_vars}")

    # Ensure shapes match
    if pred_adata.shape != truth_adata.shape:
        raise ValueError(f"Shape mismatch: {pred_adata.shape} vs {truth_adata.shape}")

    x = pred_adata.X
    y = truth_adata.X

    # Handle sparse matrices
    if hasattr(x, "toarray") or hasattr(y, "toarray"):
        x_mean = x.mean()
        y_mean = y.mean()

        x_sq_mean = x.power(2).mean() if hasattr(x, "power") else np.mean(x**2)
        y_sq_mean = y.power(2).mean() if hasattr(y, "power") else np.mean(y**2)

        if hasattr(x, "multiply"):
            xy_mean = x.multiply(y).mean()
        else:
            xy_mean = y.multiply(x).mean()

        cov = xy_mean - x_mean * y_mean
        var_x = x_sq_mean - x_mean**2
        var_y = y_sq_mean - y_mean**2

        if var_x == 0 or var_y == 0:
            return 0.0

        pearson_value = cov / np.sqrt(var_x * var_y)
        
        # Convert matrix result to scalar if necessary
        if hasattr(pearson_value, "item"):
            pearson_value = pearson_value.item()
    else:
        if np.std(x) == 0 or np.std(y) == 0:
            return 0.0
        pearson_value = np.corrcoef(x.ravel(), y.ravel())[0, 1]

    return pearson_value


if __name__ == "__main__":
    # get_score()
    predfile_path = "datasets/control_test_simulated.h5ad"
    truthfile_path = "datasets/test.h5ad"
    error = get_mse_score(predfile_path, truthfile_path)
    print(error)
    s_error = get_escore(predfile_path, truthfile_path)
    print(s_error)


