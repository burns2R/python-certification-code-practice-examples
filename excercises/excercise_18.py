import pandas as pd

df = pd.DataFrame({'Product': [' Umbrella ', ' Matress',
                               'Badminton ', 'Shuttle'],
                    'Cost': [1250, 1450, 4550, 400]})
#Correct!! the str type strip method for trimming
df['product_cleaned'] = df.Product.str.strip()
print(df)