# Landscape 

Landscape is a bioinformatic evaluation of the structure simulated protein fitness landscape
for the Protein G, B1 Domain. The landscape is created through ESM-Fold structural simulation and is
docked to a target using LightDock.

## Usage

Cleaning of Original Sequences
```
!python .\Pipeline\Sequence_Data_Cleaning.py ".\exp_data\elife-16965-supp1-v4.xlsx" .\sequence.pkl pkl 
```
Structural Simulation for experimentally derived sequences 
```
qsub run_esm_fold.sh
```

## Reference
You can reference us at:
```
Peter A. Vallet, Lane Yutzy, Stephen Wheat, and Phillip Jung,
"Landscape: A Bioinformatic Evaluation of the Structure Simulated Protein Fitness Landscape for the 
Protein G, B1 Domain", 2024, arXiv:XXXX.XXXXX [q-bio.BM] 
```

## Contact
Follow me on LinkedIn https://www.linkedin.com/in/peter-v-334609211/

