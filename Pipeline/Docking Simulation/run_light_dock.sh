#!/bin/bash
#PBS -q workq
#PBS -A hpc_gb1_re_af2
#PBS -l nodes=1:ppn=20
#PBS -l walltime=5:10:00
#PBS -o /work/pvalle6/light_dock.txt
#PBS -e /work/pvalle6/light_dock.txt
#PBS -m e
#PBS -M pvalle6@lsu.edu
#PBS -N light_dock

date
# Set some handy environment variables.
export HOME_DIR=/home/pvalle6/
export WORK_DIR=/work/pvalle6/

date
echo "Running light_dock"
cd $WORK_DIR || exit

module load python/3.8.5-anaconda-ood
source /usr/local/packages/python/3.8.5-anaconda/bin/activate landscape

for variant in $(ls ../docking_landscape/); do
    lightdock3_setup.py $(./variant/pdb_dir/variant) 2UUY_lig.pdb --noxt --noh --now -anm
    lightdock3.py setup.json -c 1 -l 0

date
echo "light_dock finished"

exit