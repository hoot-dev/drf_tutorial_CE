import requests

endpoint = 'http://localhost:8000/api/'

resp = requests.post(endpoint, json={'content': 'Hello world'})

print(resp.text)
print(f'status_code: {resp.status_code}')