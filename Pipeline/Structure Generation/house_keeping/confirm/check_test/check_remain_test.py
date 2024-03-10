"""
This script checks through the list of structures to see which ones have been generated and which have not and generates
a txt file with combo of the ones that have not been generated.

Peter Vallet 2024
"""
import pickle as pkl
import argparse
import pandas as pd
from pathlib import Path

argparse = argparse.ArgumentParser(description="This script is used to check which structures have been generated")
argparse.add_argument("exp_data", help="The path to the experimentally tested data file")
args = argparse.parse_args()

# Here the data for the experimentally tested data is loaded
with open(args.exp_data, 'rb') as f:
    exp_data = pd.read_pickle(f)
    # headers look like {Variants, HD, Count input, Count selected, Fitness, Sequence}

# create a dictionary to store the experimentally shit
structure_dictionary = {}
for row in exp_data.iterrows():
    structure_dictionary.update({row[1]["Variants"]: {"PLACEHOLDER"}})

total_counter = 0
save_dict = {}

for i in range(10):
    if i == 0:
        start = 0
        end = 14000
    elif i == 1:
        start = 14000
        end = 14000*2
    elif i == 2:
        start = 14000*2
        end = 14000*3
    elif i == 3:
        start = 14000*3
        end = 14000*4
    elif i == 4:
        start = 14000*4
        end = 14000*5
    elif i == 5:
        start = 14000*5
        end = 14000*6
    elif i == 6:
        start = 14000*6
        end = 14000*7
    elif i == 7:
        start = 14000*7
        end = 14000*8
    elif i == 8:
        start = 14000*8
        end = 14000*9
    elif i == 9:
        start = 14000*9
        end = len(structure_dictionary.keys())
    else:
        raise ValueError("The twentieth argument must be between 0 and 9")

    for combo in list(structure_dictionary.keys())[start:end]:
        combo_name_check = Path(f"./esm_fold_output/{i}_{combo}")

        if not combo_name_check.is_file():
            print(f"{i}_{combo}")
            with open("/ddnA/work/pvalle6/test_str_false.txt", "a") as f:
                f.write(f"{i}_{combo} doesn't exist\n")
        else:
            with open("/ddnA/work/pvalle6/test_str_true.txt", "a") as f:
                f.write(f"{i}_{combo} already exists\n")