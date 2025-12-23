uv run state tx infer \
  --model-dir "experiments/st-tahoe-pretrain" \
  --checkpoint "experiments/st-tahoe-pretrain/checkpoints/step=step=18000-val_loss=val_loss=0.6729.ckpt" \
  --adata "datasets/competition_support_set/competition_val_template.h5ad" \
  --embed-key "X_hvg" \
  --pert-col "target_gene" \
  --batch-col "batch_var" \
  --celltype-col "cell_type" \
  --control-pert "non-targeting" \
  --seed 42

uv run state tx infer \
  --model-dir "experiments/first_run" \
  --checkpoint "experiments/first_run/checkpoints/step=step=8000-val_loss=val_loss=1.9774.ckpt" \
  --adata "datasets/competition_support_set/competition_val_template.h5ad" \
  --pert-col "target_gene" \
  --batch-col "batch_var" \
  --celltype-col "cell_type" \
  --control-pert "non-targeting" \
  --seed 42