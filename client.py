import requests


data = {
    "name": "t05",
    "description": "d05"
}

response = requests.post('http://127.0.0.1:8000/api/products/', json=data)

if response.status_code == 201:
    print(response.json())
