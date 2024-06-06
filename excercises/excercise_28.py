import requests

BASE_URL = 'https://fakestoreapi.com'

add_product = {
    "title": 'test new product',
    "price": 14.5,
    "description": 'lorem ipsum set',
    "image": 'https://i.pravatar.cc',
    "category": 'toys'
}
# Correct!! Why? Generally, in practice, always use PUT for UPDATE operations.
# Always use POST for CREATE operations. be careful when reading the excercise,
# do they want you to update a produce or add a new one? If the latter us post!!
response = requests.post(f"{BASE_URL}/products", json=add_product)
print(response.json())