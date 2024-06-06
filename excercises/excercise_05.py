import pandas as pd

d = {
    'Name': ['Sam', 'Harry', 'Sourav', 'a', 'b', 'c'], 
    'Department': ['Administration', 'Marketing', 'Technical','Administration', 'Marketing','Administration'],
    'Salary': [120000, 50000, 70000, 50000, 50000, 50000],
    'Years of Experiance': [5, 1, 2, 1, 1, 1]
    }
df = pd.DataFrame(data=d)

#correct but with assumed data since example provided was incomplete
grouped_df = df.groupby("Department").agg({'Name': 'count', 'Salary': 'sum'})
print(grouped_df)