import requests
from getpass import getpass

auth_endpoint = 'http://localhost:8000/api/auth/'
username = input('What is your username?\n')
password = getpass('What is your password?\n')

auth_resp = requests.post(auth_endpoint, {'username': 'mhoot', 'password': password})
print(auth_resp.json())

if auth_resp.status_code == 200:
    token = auth_resp.json()['token']
    headers = {
        'Authorization': f'Bearer {token}' 
    }
    endpoint = 'http://localhost:8000/api/products/'

    resp = requests.get(endpoint, headers=headers)
    print(resp.json())
    print(f'status_code: {resp.status_code}')