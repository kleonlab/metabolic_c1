python scripts/examine_data.py \
    datasets/vcc_data/adata_Training.h5ad \
    > assets/data-info/adata_Training.out

python scripts/examine_data.py \
    datasets/competition_support_set/competition_train.h5 \
    > assets/data-info/competition_train.out

python scripts/examine_data.py \
    datasets/competition_support_set/competition_val_template.h5ad \
    > assets/data-info/competition_val_template.out

python scripts/examine_data.py \
    datasets/competition_support_set/competition_train_hvg_2000.h5ad \
    > assets/data-info/competition_train_hvg_2000.out

python scripts/examine_data.py \
    datasets/competition_support_set/jurkat.h5 \
    > assets/data-info/jurkat.out

python scripts/examine_data.py \
    datasets/competition_support_set/jurkat_hvg_2000.h5ad \
    > assets/data-info/jurkat_hvg_2000.out

python scripts/examine_data.py \
    datasets/competition_support_set/hepg2.h5 \
    > assets/data-info/hepg2.out

python scripts/examine_data.py \
    datasets/competition_support_set/hepg2_hvg_2000.h5ad \
    > assets/data-info/hepg2_hvg_2000.out
