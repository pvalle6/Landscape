#!/bin/bash
#PBS -q workq
#PBS -A hpc_gb1_re_1
#PBS -l nodes=1:ppn=20
#PBS -l walltime=5:10:00
#PBS -o /work/pvalle6/esm_output.txt
#PBS -e /work/pvalle6/esm_error.txt
#PBS -m e
#PBS -M pvalle6@lsu.edu
#PBS -N esm_fold_inf_0

date
# Set some handy environment variables.
export HOME_DIR=/home/pvalle6/
export WORK_DIR=/work/pvalle6/

date
echo "Running ESM Fold"
cd $WORK_DIR || exit

module load python/3.8.5-anaconda-ood
module load gnuparallel/20190222/intel-19.0.5

source /usr/local/packages/python/3.8.5-anaconda/bin/activate landscape

parallel python ./run_esm_inp.py ./seq_inf.pkl ./esm_fold_output_inf/ ::: {0..9}

date
echo "ESM Fold finished"

exit