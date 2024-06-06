import pandas as pd
import numpy as np
from memory_profiler import profile

from excercise_34a import process_dataa
from excercise_34b import process_datab
from excercise_34c import process_datac

df = pd.read_csv('test.csv')
cost_data = df.to_numpy()

# As you cans see in the console, b uses less memeory. B is the correct expected answer in this case. 
# Technically c could potentially use less memory, but yield returns a generator function,
# which you would then have to unpack which the example code does not do. 
process_dataa(cost_data)
process_datab(cost_data)
process_datac(cost_data)
