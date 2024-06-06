import pandas as pd

data = {'Stock': ['MSFT', 'KO', 'TSLA', 'AMZN'],
                            'Prices': [200, 50, 500, 700],
                            'Shares': [75, 200, 20, 25]}

dfa = pd.DataFrame(data)
# .dtype (which is a property present in every NumPy array)
#  or as a data frame and use .dtypes (which is a property
#  present in all Pandas objects). use dtypes attributes for pd dfs
result = dfa['Prices'].dtypes
if result == 'int64':
    print("its integer")
else:
    print("its not integer")

print(result)