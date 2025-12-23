#!/bin/bash
#SBATCH -JSlurmPythonExample                    # Job name
#SBATCH --account=gts-agarg35                   # charge account
#SBATCH -N1 --gres=gpu:RTX_6000:1                   # Number of nodes and cores per node required
#SBATCH --mem-per-gpu=80G                       # Memory per core
#SBATCH -t8:00:00                               # Duration of the job (8 hours)
#SBATCH -q embers                               # QOS Name
#SBATCH -oReport-%j.out                         # Combined output and error messages file
#SBATCH --mail-type=END,FAIL                    # Mail preferences
#SBATCH --mail-user=amete7@gatech.edu           # E-mail address for notifications
#SBATCH --output=slurm_out/Report-%A.out
cd /storage/project/r-agarg35-0/amete7/vla/st        # Change to working directory

source .venv/bin/activate

export CUDA_VISIBLE_DEVICES=0

echo "Running the following command:"

echo $@

srun $@