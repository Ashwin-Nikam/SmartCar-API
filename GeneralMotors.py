import requests
import json

BASE_URL = 'http://gmapi.azurewebsites.net'
vehicle_info = "/getVehicleInfoService"
security = "/getSecurityStatusService"
energy_level = "/getEnergyService"
engine = "/actionEngineService"


def post_request(service, id):
    request_url = BASE_URL + service
    if service == engine:
        user_input = input("Do you want to start or stop the engine? [START/STOP]")
        if user_input == 'START':
            payload = {'id': id, 'command': "START_VEHICLE",
                       'responseType': 'JSON'}
        elif user_input == 'STOP':
            payload = {'id': id, 'command': "STOP_VEHICLE",
                       'responseType': 'JSON'}
        else:
            return "Invalid input"
    else:
        payload = {'id': id, 'responseType': 'JSON'}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(request_url, headers=headers, data=json.dumps(payload)).json()
    return response
