uv run state tx infer \
  --model-dir "experiments/exp1-small" \
  --checkpoint "experiments/exp1-small/checkpoints/final.ckpt" \
  --adata "/home/b5cc/sanjukta.b5cc/metabolic_c1/datasets/control_test.h5ad" \
  --embed-key "X_hvg" \
  --pert-col "gene" \
  --batch-col "batch" \
  --celltype-col "cell_type" \
  --control-pert "NC" \
  --seed 42