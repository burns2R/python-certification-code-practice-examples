import pandas as pd
import numpy as np

survey = pd.DataFrame({'student_id': [0, 1, 2, 3],
                       'gender': [0, 1, np.nan, 3],
                       'school': [np.nan, np.nan, 2, 3],
                       'parental_educ': [0, 1, 2, np.nan],
                       'first_exam': [0, 1, np.nan, 3],
                       'second_exam': [0, 1, 2, 3]
                       })
# Correct!! supposed to use isnull() method beacause it
# returns a bolean value, so count will count all of them,
# 0 or ones, but sum() would addd them. T + F + T = T and
# 1 + 0 + 1 = 2!!
total_missing = survey.isnull().sum()
print(total_missing)