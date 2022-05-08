import requests

product_id = input('enter a product id: ')

try:
    product_id = int(product_id)
except:
    product_id = None

if product_id:
    endpoint = f'http://localhost:8000/api/products/{product_id}/delete/'

    resp = requests.delete(endpoint)

    print(f'status_code: {resp.status_code}')