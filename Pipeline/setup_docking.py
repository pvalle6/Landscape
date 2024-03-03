"""
This is a file that generates a directory structure necessary for the docking pipeline. It reads in the structural
data pickles, creates a system of folders for each.
"""
import os
import pickle as pkl
import argparse

argparse = argparse.ArgumentParser(description="This script is used to extract the")
argparse.add_argument("exp_1", help="The path to the structural data files")
argparse.add_argument("exp_2", help="The path to the structural data files")
argparse.add_argument("exp_3", help="The path to the structural data files")
argparse.add_argument("exp_4", help="The path to the structural data files")

argparse.add_argument("output", help="The path to the base of the output directory")
args = argparse.parse_args()

# read in the structural data
with open(args.exp_1, 'rb') as f:
    s_one = pkl.load(f)

if not os.path.exists(args.output):
    os.mkdir(args.output)

for key in s_one.keys():
    os.mkdir(f"{args.output}/{key}")
    # os.mkdir(f"{args.output}/{key}/structures")
    os.mkdir(f"{args.output}/{key}/pdb_dir")
    os.mkdir(f"{args.output}/{key}/docking_results")




    with open(f"{args.output}/{key}/pdb_dir/{key}.pdb", "w") as pdb_file:
        for atom_index, (x, y, z) in enumerate(s_one[key]["Structure"].positions, start=1):
            # Example PDB format line:
            # ATOM   1  N   ALA A   1      10.000  20.000  30.000  1.00  0.00
            pdb_line = f"ATOM  {atom_index:5d}  CA  UNK A   1    {x:8.3f}{y:8.3f}{z:8.3f}  1.00  0.00\n"
            pdb_file.write(pdb_line)

with open(args.exp_2, 'rb') as f:
    s_two = pkl.load(f)

for key in s_two.keys():
    os.mkdir(f"{args.output}/{key}")
    # os.mkdir(f"{args.output}/{key}/structures")
    os.mkdir(f"{args.output}/{key}/pdb_dir")
    os.mkdir(f"{args.output}/{key}/docking_results")

    with open(f"{args.output}/{key}/pdb_dir/{key}.pdb", "w") as pdb_file:
        for atom_index, (x, y, z) in enumerate(s_one[key]["Structure"].positions, start=1):
            # Example PDB format line:
            # ATOM   1  N   ALA A   1      10.000  20.000  30.000  1.00  0.00
            pdb_line = f"ATOM  {atom_index:5d}  CA  UNK A   1    {x:8.3f}{y:8.3f}{z:8.3f}  1.00  0.00\n"
            pdb_file.write(pdb_line)

with open(args.exp_3, 'rb') as f:
    s_three = pkl.load(f)

for key in s_three.keys():
    os.mkdir(f"{args.output}/{key}")
    # os.mkdir(f"{args.output}/{key}/structures")
    os.mkdir(f"{args.output}/{key}/pdb_dir")
    os.mkdir(f"{args.output}/{key}/docking_results")

    with open(f"{args.output}/{key}/pdb_dir/{key}.pdb", "w") as pdb_file:
        for atom_index, (x, y, z) in enumerate(s_one[key]["Structure"].positions, start=1):
            # Example PDB format line:
            # ATOM   1  N   ALA A   1      10.000  20.000  30.000  1.00  0.00
            pdb_line = f"ATOM  {atom_index:5d}  CA  UNK A   1    {x:8.3f}{y:8.3f}{z:8.3f}  1.00  0.00\n"
            pdb_file.write(pdb_line)

with open(args.exp_4, 'rb') as f:
    s_four = pkl.load(f)

for key in s_four.keys():
    os.mkdir(f"{args.output}/{key}")
    # os.mkdir(f"{args.output}/{key}/structures")
    os.mkdir(f"{args.output}/{key}/pdb_dir")
    os.mkdir(f"{args.output}/{key}/docking_results")

    with open(f"{args.output}/{key}/pdb_dir/{key}.pdb", "w") as pdb_file:
        for atom_index, (x, y, z) in enumerate(s_one[key]["Structure"].positions, start=1):
            # Example PDB format line:
            # ATOM   1  N   ALA A   1      10.000  20.000  30.000  1.00  0.00
            pdb_line = f"ATOM  {atom_index:5d}  CA  UNK A   1    {x:8.3f}{y:8.3f}{z:8.3f}  1.00  0.00\n"
            pdb_file.write(pdb_line)

