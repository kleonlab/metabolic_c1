uv run state tx preprocess_infer \
   --adata /home/b5cc/sanjukta.b5cc/metabolic_c1/datasets/test.h5ad \
   --output /home/b5cc/sanjukta.b5cc/metabolic_c1/datasets/test_hvg_2000.h5ad \
   --control-condition "NC" \
   --pert-col "gene" \
   --embed-key "X_hvg" \
   --seed 42