import requests

endpoint = 'http://localhost:8000/api/products/1/'

resp = requests.get(endpoint)

print(resp.json())
print(f'status_code: {resp.status_code}')