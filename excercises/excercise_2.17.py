import pandas as pd

data = {
    'Date': ['Lorem', 'Ipsum', 'is', 'simply', 'dummy', 'text', 'of', 'the', 'printing', 'and', 'typesetting', 'industry.'],
    'Region': ['Lorem', 'Ipsum', 'is', 'simply', 'dummy', 'text', 'of', 'the', 'printing', 'and', 'typesetting', 'industry.']
}
df = pd.DataFrame(data)

# Note: dtypes is obviously an attribute or property of the object. 
#Also “Object” is usually text, because str are objects in python.
# Proof:  https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dtypes.html 
# Assertion: https://www.geeksforgeeks.org/dataframe-attributes-in-python-pandas/ 
datatype_validation = df.dtypes
print(datatype_validation)