#!/bin/bash
#PBS -q single
#PBS -A hpc_gb1_re_af2
#PBS -l nodes=1:ppn=1
#PBS -l walltime=00:10:00
#PBS -o /work/pvalle6/output.txt
#PBS -e /work/pvalle6/error.txt
#PBS -j oe
#PBS -N transfer_test

date
# Set some handy environment variables.
export HOME_DIR=/home/pvalle6/
export WORK_DIR=/work/pvalle6/

cd $WORK_DIR || exit
python /work/pvalle6/lectinmat/move_to_box.py ./test_dir/ 0 1
date

exit