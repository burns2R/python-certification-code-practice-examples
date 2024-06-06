import pandas as pd
import numpy as np

d = {'Branch': ['AAA-334', 'CATX-587'], 'Employees': [35, 29], 'Sales': [467, 668]}
df = pd.DataFrame(data=d)
html = df.to_html(index=False)

sales = pd.read_html(html)

print(sales)