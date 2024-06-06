import pandas as pd
employee_service = pd.DataFrame({"employee": ["Chiva", "Otis", "Bella"], 
                                 "years_service": [2, 14, 9],
                                 "number_of_roles": [2, 3, 2]})

df = employee_service.groupby(["number_of_roles"]).sum()
print(df)
# Correct Answer is 1!! Order of columns is different beacase groupby() method makes input column the new 
# index. With the provided code as is, the resulting df is:                 
# number_of_roles             years_service
# 2                           11
# 3                           14