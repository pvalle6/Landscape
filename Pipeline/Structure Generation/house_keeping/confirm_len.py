"""
This is a script that confirms the length of the pickled data.
"""

import pickle

# Load the data
with open('../sequence.pkl', 'rb') as f:
    data = pickle.load(f)

print(data)