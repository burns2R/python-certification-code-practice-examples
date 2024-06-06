import numpy as np
import pandas as pd

d = {
    'store': ['MNO05', 'ABC01', 'MNO05', 'GHI03', 'ABC01'],
    'number_of_clients': [4, 8, 4, 8, 22],
    'date': ['2022-06-24', '2023-05-16', '2022-05-11', '2023-08-08','2023-05-16'],
    'bill_total': [127.39, 179.88, 197.12, 193.94, 193.94]
    }
df = pd.DataFrame(data=d)

#Correct! isin() method
filtered_df = df[df['store'].isin(['ABC01', 'GHI03'])]
print(filtered_df.head())