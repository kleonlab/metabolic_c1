# uv run state tx preprocess_infer \
#   --adata datasets/competition_support_set/competition_val_template.h5ad \
#   --output datasets/competition_support_set/competition_val_template_hvg_2000.h5ad \
#   --control-condition "non-targeting" \
#   --pert-col "target_gene" \
#   --embed-key "X_hvg" \
#   --seed 42