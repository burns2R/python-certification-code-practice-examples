import requests

url = 'https://jsonplaceholder.typicode.com/posts/1'
response = requests.get(url)

#Correct!!
data = response.text
print(data)