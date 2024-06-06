import pandas as pd
import os

df0 = pd.DataFrame({'Column1': [420, 380, 390],
                    'Column2': [50, 40, 45]
                    })
df0.to_csv('sample.tsv', sep='\t', index=False)

file = 'sample.tsv'
# Correct!! sep='\t' indicates a tab separated file!!
# Examples tsv or tabular files!!
df = pd.read_csv(file, sep='\t')

print(df)

os.remove('sample.tsv')