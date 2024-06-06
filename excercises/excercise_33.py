import pandas as pd

market_data = pd.DataFrame({'Stock': ['MSFT', 'KO', 'TSLA', 'AMZN'],
                            'Price': [200.23, 50.10, 500.01, 700.84],
                            'Shares': [75, 200, 20, 25]})

total_market_price = 0
# Correct!! iterrows() method Iterate over DataFrame rows 
# as (index, Series) pairs. Kinda like breaks it up that
# way!! For Dicts items() method does the same.
for index, row in market_data.iterrows():
    total_market_price += row['Price'] * row['Shares']

print("Total market price", total_market_price)