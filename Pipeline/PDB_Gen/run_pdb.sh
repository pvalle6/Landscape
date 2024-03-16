#!/bin/bash
#PBS -q workq
#PBS -A hpc_gb1_re_1
#PBS -l nodes=1:ppn=20
#PBS -l walltime=3:10:00
#PBS -o /work/pvalle6/pdb_gen.txt
#PBS -e /work/pvalle6/pdb_gen.txt
#PBS -m e
#PBS -M pvalle6@lsu.edu
#PBS -N pdb_gen

date
# Set some handy environment variables.
export HOME_DIR=/home/pvalle6/
export WORK_DIR=/work/pvalle6/

date
echo "Running PDB Generator"
cd $WORK_DIR || exit

module load python/3.8.5-anaconda-ood
module load gnuparallel/20190222/intel-19.0.5

source /usr/local/packages/python/3.8.5-anaconda/bin/activate landscape

python ./esm_to_pdb.py ./esm_fold_output/ ./pdb_test/ -1

date
echo "PDB Generator finished"

exit