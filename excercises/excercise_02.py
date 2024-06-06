import pandas as pd

d = {'Date': ['2011-12-08 00:00:00', '2008-08-13 00:00:00', '2019-09-22 00:00:00'],'Region': ['A', 'B', 'C']}
df = pd.DataFrame(data=d)
df['Date'] = pd.to_datetime(df['Date'])

df['Date'] = df['Date'].dt.strftime('%m/%d/%Y')

print(df)