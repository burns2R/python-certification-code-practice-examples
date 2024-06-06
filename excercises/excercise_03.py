import pandas as pd

d = {'Full Name': ['Tom Flint', 'Malik Patel', 'John Warby', 'Lili Chen'], 'Region': ['Region A', 'Region B', 'Region C', 'Region D']}
df = pd.DataFrame(data=d)

#Tested works Prefered
df['Region'] = df['Region'].str.replace('Region ', '')
print(df)

#Tested works
#df['Region'] = df['Region'].str[7:]
#print(df)

#Tested works
#df['Region'] = df['Region'].str.slice(7)
#print(df)