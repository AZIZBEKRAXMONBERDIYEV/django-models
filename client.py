import requests


url = 'http://127.0.0.1:8000/api/products/'


def create_product(url, data):
    response = requests.post(url, json=data)
    
    if response.status_code == 201:
        print(response.json())

data = {
    "name": "t05",
    "description": "d05"
}      
# create_product(url, data)


def get_product_all(url):
    response = requests.get(url)

    if response.status_code == 200:
        print(response.json())

# get_product_all(url)


def get_product_detial(url, pk):
    response = requests.get(f'{url}{pk}/')

    if response.status_code == 200:
        print(response.json())

# get_product_detial(url, 3)


def delete_product(url, pk):
    response = requests.delete(f'{url}{pk}/')

    if response.status_code == 205:
        print(response.json())

delete_product(url, 3)