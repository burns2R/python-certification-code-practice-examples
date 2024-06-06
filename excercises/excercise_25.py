import requests

BASE_URL = 'https://fakestoreapi.com'

product_update = {
    "title": 'updating test product',
    "category": 'appliances'
}
# Correct!! As the excercise clearly say's you need to update a file not 
# request it. Another way to see it, only 'put' method has
# json parameter becuase you are sending it somewhere to update already existing info.
response = requests.put(f"{BASE_URL}/products/21", json=product_update)
print(response.json())