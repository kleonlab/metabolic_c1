uv run state tx train \
  data.kwargs.toml_config_path="examples/hvg_2000.toml" \
  data.kwargs.embed_key="X_hvg" \
  data.kwargs.num_workers=8 \
  data.kwargs.batch_col="batch_var" \
  data.kwargs.pert_col="target_gene" \
  data.kwargs.cell_type_key="cell_type" \
  data.kwargs.control_pert="non-targeting" \
  data.kwargs.perturbation_features_file="datasets/competition_support_set/ESM2_pert_features.pt" \
  training.max_steps=40000 \
  training.ckpt_every_n_steps=20000 \
  model=state_sm \
  use_wandb=false \
  wandb.tags="[dry_run]" \
  wandb.project=state-arc \
  wandb.entity=a-mete-2416 \
  output_dir="experiments/" \
  name="dry_run"