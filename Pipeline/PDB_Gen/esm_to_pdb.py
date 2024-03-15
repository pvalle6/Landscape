"""
This is the script for converting the HuggingFace port of ESM-fold generated structures to PDB files. The code is
from their soon-to-be implemented function for doing the same.

Peter Vallet
"""

import argparse
import os
import pickle
from transformers.models.esm.openfold_utils.protein import to_pdb, Protein as OFProtein
from transformers.models.esm.openfold_utils.feats import atom14_to_atom37


argparse = argparse.ArgumentParser(description="This script is used to convert the "
                                               "outputs from the ESM0fold model to PDB files")
argparse.add_argument("fpath", help="The path to the structures folder")
argparse.add_argument("output", help="The path to the output folder")
argparse.add_argument("range", help="range of structures to convert to PDB files")
args = argparse.parse_args()

parsed_int = int(args.range)

if parsed_int == 0:
    start = 0
    end = 14000
elif parsed_int == 1:
    start = 14000
    end = 14000*2
elif parsed_int == 2:
    start = 14000*2
    end = 14000*3
elif parsed_int == 3:
    start = 14000*3
    end = 14000*4
elif parsed_int == 4:
    start = 14000*4
    end = 14000*5
elif parsed_int == 5:
    start = 14000*5
    end = 14000*6
elif parsed_int == 6:
    start = 14000*6
    end = 14000*7
elif parsed_int == 7:
    start = 14000*7
    end = 14000*8
elif parsed_int == 8:
    start = 14000*8
    end = 14000*9
elif parsed_int == 9:
    start = 14000*9
    end = 149361
else:
    raise ValueError("The twentieth argument must be between 0 and 9")


def convert_esm_to_pdb(outputs):
    """
    This function converts the outputs from the ESM-fold model to PDB files.

    It has been modified to detach the gradient function from the tensors and convert them to numpy arrays.
    :param outputs:
    :return:
    """
    final_atom_positions = atom14_to_atom37(outputs["positions"][-1], outputs)
    outputs = {k: v.to("cpu").detach().numpy() for k, v in outputs.items()}
    final_atom_positions = final_atom_positions.cpu().detach().numpy()
    final_atom_mask = outputs["atom37_atom_exists"]
    pred = None
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
    if pred is not None:
        pdb = to_pdb(pred)
        with open(f"./{args.output}/{list(all_data.keys())[0]}.pdb", "w") as f:
            for item in pdb:
                f.write(item)


all_data = {}
for file in os.listdir(args.fpath)[start:end]:
    with open(os.path.join(args.fpath, file), "rb") as f:
        structure = pickle.load(f)
        variant = list(structure.keys())[0]
        all_data.update({variant: {"Structure": structure[variant]["Structure"],
                                   "Fitness": structure[variant]["Fitness"]}})
        convert_esm_to_pdb(all_data[list(all_data.keys())[0]]["Structure"])
        all_data = {}
        print(f"Converted {file} to PDB file")
