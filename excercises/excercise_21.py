import pandas as pd 
import numpy as np

df = pd.DataFrame(np.random.randint(0,3,size=(3, 2)), columns=list('AB'))
# Correct!! You print the array size with the shape attibute! Remember an atribute is a characterisric of 
# an object, so no () in general.
print(df.shape)