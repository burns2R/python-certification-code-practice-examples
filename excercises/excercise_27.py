import pandas as pd

student_df = pd.DataFrame({'Name': ['Tom', 'Malik', 'John', 'Lilli'],
                           'Location': ['France', 'Canada', 'UK', 'China']})


age_df = pd.DataFrame({'Name': ['Alex', 'Malik', 'John', 'Lilli'],
                       'Age': [18, 19, 17, 21]})
# Correct!! Trick answer!! Should be outer to include all the 'Names'
# existing in the two dataframes.
inner_joined = student_df.merge(age_df, on=['Name'], how='outer')
print(inner_joined)