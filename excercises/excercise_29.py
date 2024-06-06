import pandas as pd
import numpy as np

df = pd.DataFrame({'name': [1, 2, 3],
                   'Column': [4, 5, np.nan]})
# Correct classic .isna().sum() chained method wombocombo
# that Datacamp loves!
NullCount = df['name'].isna().sum()
if NullCount < 1:
    print("column not null")
else:
    print("column is null")