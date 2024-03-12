#!/bin/bash
#PBS -q workq
#PBS -A hpc_gb1_re_1
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
cd $WORK_DIR/light_dock_dir/ || exit

module load python/3.8.5-anaconda-ood
source /usr/local/packages/python/3.8.5-anaconda/bin/activate landscape

for variant in $(ls ../tested_pdbs/); do
    # noxt removes oxygen atoms, noh removes hydrogen atoms, now removes crystal water molecules

    lightdock3_setup.py $(./variant/pdb_dir/variant) 2UUY_lig.pdb --noxt --noh --now -anm
    lightdock3.py setup.json -c 1 -l 0
    lgd_generate_conformations.py variant 2UUY_lig.pdb
    lgd_cluster_bsas.py gso_5.out

date
echo "light_dock finished"

exit