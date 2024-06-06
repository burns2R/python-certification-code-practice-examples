import pandas as pd
data = {
    'Resource': ['CPU', 'Memory', 'Disk', 'Network', 'CPU'],
    'Utilization': [70, 60, 30, 15, 10]
}
df = pd.DataFrame(data)

# Note: Seems all it needs is the for statement to complete the list comprehension.
# Proof: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
# Assertion: https://stackoverflow.com/questions/52437024/python-list-comprehension-with-loop-over-dataframe
total_cpu_utilization = sum([row['Utilization'] for index, row in df.iterrows() if row['Resource'] == 'CPU'])

print('Total CPU utilization: ', total_cpu_utilization)