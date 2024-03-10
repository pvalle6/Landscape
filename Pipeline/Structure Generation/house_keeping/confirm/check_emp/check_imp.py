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
argparse.add_argument("exp_data", help="The path to the impted data file")
args = argparse.parse_args()

# Here the data for the experimentally tested data is loaded
with open(args.exp_data, 'rb') as f:
    exp_data = pd.read_pickle(f)
    # headers look like {Variants, HD, Count input, Count selected, Fitness, Sequence}

# create a dictionary to store the experimentally shit
structure_dictionary = {}
for row in exp_data.iterrows():
    structure_dictionary.update({row[1]["Variants"]: {"PLACEHOLDER"}})

size_str = len(structure_dictionary.keys())
total = 0
save_dict = {}
inter = 1000
count_true = 0
count_false = 0
for i in range(10):
    if i == 0:
        start = 0
        end = inter
    elif i == 1:
        start = inter
        end = inter*2
    elif i == 2:
        start = inter*2
        end = inter*3
    elif i == 3:
        start = inter*3
        end = inter*4
    elif i == 4:
        start = inter*4
        end = inter*5
    elif i == 5:
        start = inter*5
        end = inter*6
    elif i == 6:
        start = inter*7
        end = inter*8
    elif i == 7:
        start = inter*8
        end = inter*9
    elif i == 8:
        start = inter*8
        end = inter*9
    elif i == 9:
        start = inter*9
        end = len(structure_dictionary.keys())
    else:
        raise ValueError("The twentieth argument must be between 0 and 9")
    for combo in list(structure_dictionary.keys())[start:end]:
        combo_name_check = Path(f"./esm_fold_output_inf/{i}_{combo}")

        if not combo_name_check.is_file():
            count_false = count_false + 1
            total = total + 1
            with open("/ddnA/work/pvalle6/imp_str_false.txt", "a") as f:
                f.write(f"{i}_{combo} doesn't exist\n")
        else:
            count_true = count_true + 1
            total = total + 1
            with open("/ddnA/work/pvalle6/imp_str_true.txt", "a") as f:
                f.write(f"{i}_{combo} already exists\n")

print("true " + str(count_true))
print("false " + str(count_false))
print(total)
print(size_str)