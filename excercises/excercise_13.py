import pandas as pd
import numpy as np

df = pd.DataFrame({'column one': [0.430473, np.nan,
                                  -0.520513, np.nan,
                                  0.816822, np.nan],
                    'column two': [0.982138, np.nan,
                                   0.341685, np.nan,
                                   -1.5588, np.nan]
                    }, index=['a', 'b','c', 'd', 'e', 'f'])
#Correct! want to fill na/null values of col1 with mean values of column one!!
df["column one"] = df["column one"].fillna(df["column one"].mean())
print(df)