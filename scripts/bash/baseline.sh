cell-eval baseline \
    -a datasets/competition_support_set/hepg2.h5 \
    -t 32 \
    -o cell-eval-outdir/hepg2/baseline/

cell-eval run \
  -ap cell-eval-outdir/hepg2/baseline/baseline.h5ad \
  -ar datasets/competition_support_set/hepg2.h5 \
  -dp cell-eval-outdir/hepg2/baseline/baseline_de.csv \
  --skip-metrics clustering_agreement,pearson_edistance \
  --num-threads 32 \
  -o cell-eval-outdir/hepg2/baseline/
