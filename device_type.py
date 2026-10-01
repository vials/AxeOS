import requests

response = requests.get(f'http://X.X.X.X/api/system/asic') # Replace with your IP

print(response.json().get("deviceModel"))
