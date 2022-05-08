import requests

endpoint = 'http://localhost:8000/api/products/'

content = {
    'title': 'a fun new title',
    'price': 39.95
}

resp = requests.post(endpoint, json=content)

print(resp.json())
print(f'status_code: {resp.status_code}')