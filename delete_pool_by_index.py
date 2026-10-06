import requests
#index starts at 0
index = 1

response = requests.delete(f'http://X.X.X.X/api/system/pools/{index}')  # Replace with your IP
print(response.text)
