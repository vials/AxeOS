import requests

#Requires payload to be generated from fetch_pool_settings.py
#json_data = payload

response = requests.patch('http://X.X.X.X/api/system', json=json_data) # Replace with your IP
print(response.text)
