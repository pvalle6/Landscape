#!/bin/bash
#PBS -q single
#PBS -A hpc_gb1_re_af2
#PBS -l nodes=1:ppn=1
#PBS -l walltime=00:10:00
#PBS -o /home/pvalle6/output.txt
#PBS -e /home/pvalle6/error.txt
#PBS -j oe
#PBS -N rm_script

date
# Set some handy environment variables.
export HOME_DIR=/home/pvalle6/
export WORK_DIR=/work/pvalle6/

cd HOME_DIR || exit
rm -r -d /home/pvalle6/lectinmat/
date

exit