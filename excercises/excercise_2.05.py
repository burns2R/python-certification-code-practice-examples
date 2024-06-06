import pandas as pd

data = [
    {
        "id": 131,
        "name": "Mia",
        "measurements": {"height": 157, "weight": 52},
    },
    {
        "id": 132,
        "name": "Sebastian",
        "measurements": {"height": 165, "weight": 63},
    },
    {
        "id": 133,
        "name": "Andrew",
        "measurements": {"height": 179, "weight": 72},
    }
]

# Correct!!
# Proof: https://pandas.pydata.org/docs/reference/api/pandas.json_normalize.html
# Assertion: https://www.geeksforgeeks.org/converting-nested-json-structures-to-pandas-dataframes/ 

result = pd.json_normalize(data, max_level=1)
print(result)