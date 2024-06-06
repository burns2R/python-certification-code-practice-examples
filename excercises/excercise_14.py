import pandas as pd
import json

dict = {'name': ['Mark', 'Jane', 'Mia'],
        'Score': [78, 89, 64]}
data_json = json.dumps(dict)

df = pd.read_json(data_json)
print(df)