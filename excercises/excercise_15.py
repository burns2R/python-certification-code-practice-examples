import pandas as pd
import numpy as np

df = pd.DataFrame({'col1': [0, np.nan, np.nan, 3, 4],
                   'col2': [0, 1, 2, np.nan, np.nan],
                   'col3': [4, np.nan, np.nan, 7, 10]})

df = df.interpolate(method='linear')

print(df)