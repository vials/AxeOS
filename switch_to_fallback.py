import requests

response = requests.patch('http://X.X.X.X/api/system', json={'useFallbackStratum': 1}) # Replace with your IP. 1 = True, 0 = False
print(response.text)
