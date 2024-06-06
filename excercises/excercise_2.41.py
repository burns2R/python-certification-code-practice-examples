import pandas as pd

patients = pd.DataFrame({'Name': ['Ahmed', 'Emily', 'Marco', 'Juan', 'Wei'],
                         'Height(cm)': [175, 162, 180, 165, 185],
                         'Weight(kg)': [70, 56, 75, 62, 80],
                         'BMI': [22.85, 21.34, 23.15, 22.77, 32.14]})

# Note: Simple make a function call “get_bmi_over_30(df)”
# Proof: https://www.w3schools.com/python/python_functions.asp 
def get_bmi_over_30(df):
    filtered = df[df['BMI'] > 30]
    names = filtered['Name'].tolist()
    print(names)

get_bmi_over_30(patients)
