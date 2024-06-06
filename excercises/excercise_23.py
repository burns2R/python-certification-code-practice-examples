import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.random.randint(0,100,size=(3, 2)), columns=list('AB'))
df2 = pd.DataFrame(np.random.randint(0,100,size=(3, 2)), columns=list('AB'))
#Correct!! We use concat instead of stack? since it is getting devaluated.
union_df = pd.concat([df1, df2])
print(union_df)