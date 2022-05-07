import requests

endpoint = 'http://localhost:8000/api/'

resp = requests.get(endpoint, params={'q': 'search'}, json={'something': 'nothing'})

print(resp.text)
print(f'status_code: {resp.status_code}')