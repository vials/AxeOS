import requests
#index starts at 0
index = 1

response = requests.delete(f'http://192.168.1.30/api/system/pools/{index}')
print(response.text)
