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

argparse = argparse.ArgumentParser(description="This script is used to extract the"
                                               "sequence data from the two eLife SI files")
argparse.add_argument("exp_data", help="The path to the experimental data file")
argparse.add_argument("output", help="The path to the output file")
argparse.add_argument("fourth", help="Which 1/4 of the data to process (1, 2, 3, 4)")
args = argparse.parse_args()

with open(args.exp_data, 'rb') as f:
    exp_data = pkl.load(f)
    # headers look like {Variants, HD, Count input, Count selected, Fitness, Sequence}

# create a dictionary to store the data
structure_dictionary = {}
for row in exp_data.iterrows():
    structure_dictionary.update({row[1]["Variants"]: {"Sequence": row[1]["Sequence"], "Fitness": row[1]["Fitness"]}})

model = EsmForProteinFolding.from_pretrained("facebook/esmfold_v1")
tokenizer = AutoTokenizer.from_pretrained("facebook/esmfold_v1")


def predict_structure(sequence: str, model, tokenizer):
    inputs = tokenizer([sequence], return_tensors="pt", add_special_tokens=False)
    outputs = model(**inputs)
    return outputs


total_counter = 0
save_dict = {}

if args.fourth == "1":
    start = 0
    end = int(len(structure_dictionary)/4)
elif args.fourth == "2":
    start = int(len(structure_dictionary)/4)
    end = int(len(structure_dictionary)/2)
elif args.fourth == "3":
    start = int(len(structure_dictionary)/2)
    end = int(len(structure_dictionary)/4)*3
elif args.fourth == "4":
    start = int(len(structure_dictionary)/4)*3
    end = len(structure_dictionary)
else:
    raise ValueError("The fourth argument must be 1, 2, 3, or 4")

for combo in list(structure_dictionary.keys())[start:end]:
    total_counter += 1
    save_dict.update(
        {combo: {"Structure": predict_structure(structure_dictionary[combo]["Sequence"], model, tokenizer),
                 "Fitness": structure_dictionary[combo]["Fitness"]}})
    if total_counter % 100 == 0:
        print(f"Predicted {total_counter} structures")

with open(f"{args.fourth}_{total_counter}_{args.output}", 'wb') as f:
    pkl.dump(save_dict, f)
