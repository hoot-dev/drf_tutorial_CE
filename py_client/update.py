import requests

endpoint = 'http://localhost:8000/api/products/1/update/'

data = {
    'title': 'An Updated Title',
    'price': 129.99
}

resp = requests.put(endpoint, json=data)

print(resp.json())
print(f'status_code: {resp.status_code}')