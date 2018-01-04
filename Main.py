import requests
import json

BASE_URL = 'http://gmapi.azurewebsites.net'
vehicle_info = "/getVehicleInfoService"
security = "/getSecurityStatusService"
energy_level = "/getEnergyService"
engine = "/actionEngineService"


def gm_api_post(service):
    request_url = BASE_URL + service
    if service == engine:
        payload = {'id': '1234', 'command': "START_VEHICLE|STOP_VEHICLE",
                   'responseType': 'JSON'}
    else:
        payload = {'id': '1234', 'responseType': 'JSON'}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(request_url, headers=headers, data=json.dumps(payload)).json()
    return response


print(gm_api_post(vehicle_info))
print()
print(gm_api_post(security))
print()
print(gm_api_post(energy_level))