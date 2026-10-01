import requests

response = requests.get('http://X.X.X.X/api/system/info') # Replace with your IP
print(f"[{response.status_code}] = {response.text}")
