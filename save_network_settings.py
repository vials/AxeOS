import requests

json_data = {
    'hostname': 'gammahex', # Change hostname to whatever you want
    'ssid': 'NETWORK_NAME', # Enter Wifi name
    'wifiPass': 'PASSWORD', # Enter password for Wifi
}

response = requests.patch('http://X.X.X.X/api/system', json=json_data) # Replace with your IP
print(response.text)
