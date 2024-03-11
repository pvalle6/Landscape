"""
This is the script for converting the HuggingFace port of ESM0fold generated structures to PDB files. The code is
from their soon-to-be implemented function for doing the same.

Peter Vallet
"""

import argparse
import os
import numpy as np
import pickle
import torch
from sklearn.decomposition import IncrementalPCA, PCA
import transformers
from transformers import AutoTokenizer, EsmForProteinFolding
from transformers.models.esm.openfold_utils.protein import to_pdb, Protein as OFProtein
from transformers.models.esm.openfold_utils.feats import atom14_to_atom37


argparse = argparse.ArgumentParser(description="This script is used to convert the "
                                               "outputs from the ESM0fold model to PDB files")
argparse.add_argument("fpath", help="The path to the structures folder")
argparse.add_argument("output", help="The path to the output file")
args = argparse.parse_args()

all_data = {}
for file in os.listdir(args.fpath):
    with open(os.path.join(args.fpath, file), "rb") as f:
        structure = pickle.load(f)
        variant = list(structure.keys())[0]
        all_data.update({variant: {"Structure": structure[variant]["Structure"],
                                   "Fitness": structure[variant]["Fitness"]}})


def convert_outputs_to_pdb(outputs):
    """
    This function converts the outputs from the ESM0fold model to PDB files.

    It has been modified to detach the gradient function from the tensors and convert them to numpy arrays.
    :param outputs:
    :return:
    """
    final_atom_positions = atom14_to_atom37(outputs["positions"][-1], outputs)
    outputs = {k: v.to("cpu").detach().numpy() for k, v in outputs.items()}
    final_atom_positions = final_atom_positions.cpu().detach().numpy()
    final_atom_mask = outputs["atom37_atom_exists"]
    pdbs = []
    for i in range(outputs["aatype"].shape[0]):
        aa = outputs["aatype"][i]
        pred_pos = final_atom_positions[i]
        mask = final_atom_mask[i]
        resid = outputs["residue_index"][i] + 1
        pred = OFProtein(
            aatype=aa,
            atom_positions=pred_pos,
            atom_mask=mask,
            residue_index=resid,
            b_factors=outputs["plddt"][i],
            chain_index=outputs["chain_index"][i] if "chain_index" in outputs else None,
        )
        pdbs.append(to_pdb(pred))
    return pdbs

# pdb = convert_outputs_to_pdb(all_data[list_keys_all_data[0]]["Structure"])
