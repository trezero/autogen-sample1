# filename: download_swagger.py
import requests
import json

url = 'your_swagger_url'  # replace 'your_swagger_url' with the actual URL
response = requests.get(url)
swagger = response.json()

with open('swagger.json', 'w') as f:
    json.dump(swagger, f)