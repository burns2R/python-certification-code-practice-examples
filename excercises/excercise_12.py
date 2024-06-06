import pandas as pd

df = pd.DataFrame({'a': [1,2,1,2,1,2],
                   'b': [True, False, True, False, True, False],
                   'c': [1,2,1,2,1,2]
                   })

#Correct!!
df_integer = df.select_dtypes(include=['int'])
print(df_integer)