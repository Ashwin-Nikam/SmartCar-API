import requests
import json

BASE_URL = 'http://gmapi.azurewebsites.net'

request_url = BASE_URL + "/getVehicleInfoService"
payload = {'id': '1234', 'responseType': 'JSON'}
headers = {'Content-Type': 'application/json'}
user_info = requests.post(request_url, headers=headers, data=json.dumps(payload)).json()
print(user_info)