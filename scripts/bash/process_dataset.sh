uv run state tx preprocess_train \
  --adata datasets/competition_support_set/competition_train.h5 \
  --output datasets/competition_support_set/competition_train_hvg_2000.h5ad \
  --num_hvgs 2000

uv run state tx preprocess_train \
  --adata datasets/competition_support_set/k562_gwps.h5 \
  --output datasets/competition_support_set/k562_gwps_hvg_2000.h5ad \
  --num_hvgs 2000

uv run state tx preprocess_train \
  --adata datasets/competition_support_set/rpe1.h5 \
  --output datasets/competition_support_set/rpe1_hvg_2000.h5ad \
  --num_hvgs 2000

uv run state tx preprocess_train \
  --adata datasets/competition_support_set/jurkat.h5 \
  --output datasets/competition_support_set/jurkat_hvg_2000.h5ad \
  --num_hvgs 2000

uv run state tx preprocess_train \
  --adata datasets/competition_support_set/k562.h5 \
  --output datasets/competition_support_set/k562_hvg_2000.h5ad \
  --num_hvgs 2000

uv run state tx preprocess_train \
  --adata datasets/competition_support_set/hepg2.h5 \
  --output datasets/competition_support_set/hepg2_hvg_2000.h5ad \
  --num_hvgs 2000

uv run state tx preprocess_train \
  --adata datasets/competition_support_set/competition_val_template.h5ad \
  --output datasets/competition_support_set/competition_val_template_hvg_2000.h5ad \
  --num_hvgs 2000