import pandas as pd

data = {
    'Column A': [1, 2, 3],
    'Column B': ['A', 'B', 'C']
}
df = pd.DataFrame(data)

# Note: Asking for the number of rows and columns, not to iterate over them
# Proof: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shape.html#pandas.DataFrame.shape
# Assertion: https://note.nkmk.me/en/python-pandas-len-shape-size/#get-the-number-of-rows-and-columns-dfshape 
rows, columns = df.shape

print('columns = ', columns, 'rows = ', rows)