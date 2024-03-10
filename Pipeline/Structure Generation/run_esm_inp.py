"""
This script calls the pretrained EsmFold model to predict the structure of provided sequences.
The sequences are provided in a pickled pandas dataframe.

The output is in a pickled dictionary with the key being the 4 letter mutated name and the value being
the sequence, fitness score, and predicted structure.

Peter Vallet 2024
"""
import pickle as pkl
import argparse
import pandas
from transformers import AutoTokenizer, EsmForProteinFolding
from pathlib import Path

argparse = argparse.ArgumentParser(description="This script is used to extract the"
                                               "sequence data from the two eLife SI files")
argparse.add_argument("exp_data", help="The path to the experimental data file")
argparse.add_argument("output", help="The path to the output file")
argparse.add_argument("p_group", help="Which 1/10 of the data to process (0-9)")
args = argparse.parse_args()

with open(args.exp_data, 'rb') as f:
    exp_data = pkl.load(f)
    # headers look like {Variants, HD, Count input, Count selected, Fitness, Sequence}

# create a dictionary to store the data
structure_dictionary = {}
for row in exp_data.iterrows():
    structure_dictionary.update({row[1]["Variants"]: {"Sequence": row[1]["Sequence"], "Imputed fitness": row[1]["Imputed fitness"]}})

model = EsmForProteinFolding.from_pretrained("facebook/esmfold_v1")
tokenizer = AutoTokenizer.from_pretrained("facebook/esmfold_v1")


def predict_structure(sequence: str, model, tokenizer):
    inputs = tokenizer([sequence], return_tensors="pt", add_special_tokens=False)
    outputs = model(**inputs)
    return outputs


total_counter = 0
save_dict = {}

parsed_int = int(args.p_group)

inter = 1000
if parsed_int == 0:
    start = 0
    end = inter
elif parsed_int == 1:
    start = inter
    end = inter*2
elif parsed_int == 2:
    start = inter*2
    end = inter*3
elif parsed_int == 3:
    start = inter*3
    end = inter*4
elif parsed_int == 4:
    start = inter*4
    end = inter*5
elif parsed_int == 5:
    start = inter*5
    end = inter*6
elif parsed_int == 6:
    start = inter*6
    end = inter*7
elif parsed_int == 7:
    start = inter*7
    end = inter*8
elif parsed_int == 8:
    start = inter*8
    end = inter*9
if parsed_int == 9:
    start = inter*9
    end = len(structure_dictionary.keys())

for combo in list(structure_dictionary.keys())[start:end]:
    combo_name_check = Path(f"{args.output}{parsed_int}_{combo}")
    if not combo_name_check.is_file():
        # file exists
        output = {combo: {"Structure": predict_structure(structure_dictionary[combo]["Sequence"], model, tokenizer),
                          "Imputed fitness": structure_dictionary[combo]["Imputed fitness"]}}

        with open(f"{args.output}{args.p_group}_{combo}", 'wb') as f:
            pkl.dump(output, f)
