import pandas as pd
import numpy as np

data = {
    'student': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'gender': [1, 1, 1, 1, 1, 1, np.NAN, 1, 1, 1],
    'school': [1, 1, 1, 1, 1, 1, 1, 1, np.NAN, 1],
    'parental_educ': [1, 1, 1, 1, np.NAN, 1, 1, 1, 1, 1],
    'first_exam': [1, 1, 1, 1, np.NAN, 1, 1, 1, 1, 1],
    'second_exam': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    }
survey = pd.DataFrame(data)

# Note! Should be notna!!!! Get a list that displays True for all the elements in the data frame not containing null values.
non_missing = survey.notna()
print(non_missing)