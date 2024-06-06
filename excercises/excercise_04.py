import pandas as pd

d = {
    'Product': ['UMbreLla', 'maTress', 'baDmintoN', 'Shuttle'], 
    'Cost': [1250, 1450, 1550, 400]
    }
df = pd.DataFrame(data=d)

#works prefared
df['Product_cleaned'] = df.Product.str.title()
print(df)

#works
#df['Product_cleaned'] = df.Product.str.capitalize()
#print(df)