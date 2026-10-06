import requests

response = requests.get('http://X.X.X.X/api/system/wifi/scan') # Replace with your IP

for network in response.json()['networks']:
    print(f"SSID: {network.get('ssid')} | RSSI: {network.get('rssi')} | Auth Mode: {network.get('authmode')}")
