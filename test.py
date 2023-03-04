import requests
from pprint import pprint

data = {"prompt": "What is python?"}
response = requests.post('http://localhost:8000/generate', json=data)
pprint(response.text)

