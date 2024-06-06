import pandas as pd
import os

df0 = pd.DataFrame({'Column1': [420, 380, 390],
                    'Column2': [50, 40, 45]
                    })
df0.to_csv('sample.csv', index=False)

file = 'sample.csv'
# Correct!! Should be header=none, not 0 or False. Follows provided expeted result.
df = pd.read_csv(file, header=None)

print(df)

os.remove('sample.csv')