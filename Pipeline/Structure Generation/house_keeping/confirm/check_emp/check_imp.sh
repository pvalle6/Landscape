#!/bin/bash
#PBS -q single
#PBS -A hpc_gb1_re_1
#PBS -l nodes=1:ppn=1
#PBS -l walltime=0:10:00
#PBS -o /work/pvalle6/check_output.txt
#PBS -e /work/pvalle6/check_error.txt
#PBS -m e
#PBS -M pvalle6@lsu.edu
#PBS -N check_r

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

python ./check_imp.py ./sequence_inf.pkl

date
echo "ESM Fold finished"

exit