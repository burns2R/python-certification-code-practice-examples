import pandas as pd

df = pd.DataFrame({'Column A': [6, 5, 4, 4, 3], 'Column B': ['F', 'A', 'D', 'D', 'C']})
# Correct!! Highly likely we need to specify the "keep" parameter because if we assume the rest of the df has 
# no duplicates,the expected return should be at least 2 and the default parameter 'first' returns 1. 
# Read doc for more info.

count_duplicates = df.duplicated(keep=False).sum()
print(count_duplicates)
