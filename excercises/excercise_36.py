import pandas as pd

patients = pd.DataFrame({'Name': ['Ahmed', 'Emily', 'Marco', 'Juan', 'Wei'],
                         'Height(cm)': [175, 162, 180, 165, 185],
                         'Weight(kg)': [70, 56, 75, 62, 80]})

def calculate_bmi(weight, height):
    return weight / (height / 100) ** 2
# Correct!!! While other methos can take lambda functions as
# a parameter, apply is the the only one  that seemingly takes
# axis parameter. The round() method not expected but necesary to match example output
patients['BMI'] = patients.apply(lambda row: calculate_bmi(row['Weight(kg)'], row['Height(cm)']), axis=1).round(2)

print(patients)