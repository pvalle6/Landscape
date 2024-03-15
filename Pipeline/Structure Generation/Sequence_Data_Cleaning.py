"""
This is the first python script in the pipeline. It is used to extract the sequence data from the two eLife SI files

experimentally derived: elife-16965-supp1-v4.xlsx and imputed values: elife-16965-supp2-v4.xlsx.

Peter Vallet 2024
"""
from logging import exception
import pandas as pd
import pickle as pkl
import openpyxl
from tqdm import tqdm
import argparse

# Here is the full sequence for the WT protein GB1 from csb.org/sequence/3GB1
# >3GB1_1|Chain A|PROTEIN (B1 DOMAIN OF STREPTOCOCCAL PROTEIN G)|Streptococcus sp. 'group G' (1320)
# MTYKLILNGKTLKGETTTEAVDAATAEKVFKQYANDNGVDGEWTYDDATKTFTVTE

argparse = argparse.ArgumentParser(description="This script is used to extract the"
                                               "sequence data from the two eLife SI files")
argparse.add_argument("exp_data", help="The path to the experimental data file")
argparse.add_argument("output", help="The path to the output file")
argparse.add_argument("output_file_type",
                      choices=("xlsx", "csv", "pkl"), help="The type of the output file")
args = argparse.parse_args()


def generate_sequence_variants(data: pd.DataFrame, sequence: str) -> list:
    """
    This function takes in the experimental data and the wild type sequence and generates a list of the sequence
    variants for the given site, in the order given in the Excel sheet.
    """

    # Epistatic Sites are at V39, D40, G41, V54
    # here all are less 1 because of 0 indexing
    site_v39 = 38
    # site_d40 = 39
    site_g41 = 40
    site_v54 = 53

    # create a list to store the variants
    sequence_variants = []
    for row in tqdm(data.iterrows()):
        # get the mutation
        mutated_residues = row[1]
        mutated_v39 = mutated_residues["Variants"][0]
        mutated_v40 = mutated_residues["Variants"][1]
        mutated_v41 = mutated_residues["Variants"][2]
        mutated_v54 = mutated_residues["Variants"][3]

        mutated_seq = (sequence[:site_v39] + mutated_v39 + mutated_v40 + mutated_v41 +
                       sequence[site_g41+1: site_v54] + mutated_v54 + sequence[site_v54+1:])
        sequence_variants.append(mutated_seq)

        # if sequence_variants[0] != sequence:
        #     exception("The sequence is not correct")
    return sequence_variants


# read in the experimental data
exp_data = pd.read_excel(args.exp_data)z
wt_sequence = "MTYKLILNGKTLKGETTTEAVDAATAEKVFKQYANDNGVDGEWTYDDATKTFTVTE"

exp_data.insert(2, "Sequence", generate_sequence_variants(exp_data, wt_sequence))

# save the data
if args.output_file_type == "pkl":
    with open(args.output, 'wb') as f:
        pkl.dump(exp_data, f)
if args.output_file_type == "csv":
    exp_data.to_csv(args.output, index=False)
if args.output_file_type == "xlsx":
    exp_data.to_excel(args.output, index=False)

print("Sequences Added!")
