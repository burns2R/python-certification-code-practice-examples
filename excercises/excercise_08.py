import requests

url = 'https://jsonplaceholder.typicode.com/todos'
# correct params is the correct A dictionary, 
# list of tuples or bytes to send as a query string.
# available params to more precise query will be available 
# in the target api's documentation
response = requests.get(url, params={'userId': 1})
data = response.json()

print(data)