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

# Here is the full sequence for the WT protein GB1 from csb.org/sequence/3GB1
# >3GB1_1|Chain A|PROTEIN (B1 DOMAIN OF STREPTOCOCCAL PROTEIN G)|Streptococcus sp. 'group G' (1320)
# MTYKLILNGKTLKGETTTEAVDAATAEKVFKQYANDNGVDGEWTYDDATKTFTVTE

argparse = argparse.ArgumentParser(description="This script is used to extract the"
                                               "sequence data from the two eLife SI files")
argparse.add_argument("exp_data", help="The path to the experimental data file")
argparse.add_argument("output", help="The path to the output file")
argparse.add_argument("output_file_type",
                      choices="pkl", help="The type of the output file")
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

for combo in structure_dictionary.keys():
    structure_dictionary.update(
        {combo: {"Structure": predict_structure(structure_dictionary[combo]["Sequence"], model, tokenizer)}})

# save the data
if args.output_file_type == "pkl":
    with open(args.output, 'wb') as f:
        pkl.dump(structure_dictionary, f)
