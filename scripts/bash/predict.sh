cell-eval score \
    -o cell-eval-outdir/hepg2/st-tahoe-pretrain/baseline_diff.csv \
    --user-input experiments/st-tahoe-pretrain/eval_step=step=18000-val_loss=val_loss=0.6729.ckpt/hepg2_agg_results.csv \
    --base-input cell-eval-outdir/hepg2/baseline/agg_results.csv

cell-eval score \
    -o cell-eval-outdir/hepg2/first_run/baseline_diff.csv \
    --user-input experiments/first_run/eval_step=step=8000-val_loss=val_loss=1.9774.ckpt/hepg2_agg_results.csv \
    --base-input cell-eval-outdir/hepg2/baseline/agg_results.csv


uv run state tx predict \
    --output-dir "experiments/st-tahoe-pretrain" \
    --checkpoint "step=step=18000-val_loss=val_loss=0.6729.ckpt"

uv run state tx predict \
    --output-dir "experiments/first_run" \
    --checkpoint "step=step=8000-val_loss=val_loss=1.9774.ckpt"

