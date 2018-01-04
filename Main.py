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
        user_input = input("Do you want to start or stop the engine? [START/STOP]")
        if user_input == 'START':
            payload = {'id': '1234', 'command': "START_VEHICLE",
                       'responseType': 'JSON'}
        elif user_input == 'STOP':
            payload = {'id': '1234', 'command': "STOP_VEHICLE",
                       'responseType': 'JSON'}
        else:
            return "Invalid input"
    else:
        payload = {'id': '1234', 'responseType': 'JSON'}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(request_url, headers=headers, data=json.dumps(payload)).json()
    return response


def test_gm_api():
    print(gm_api_post(vehicle_info))
    print()
    print(gm_api_post(security))
    print()
    print(gm_api_post(energy_level))
    print()
    print(gm_api_post(engine))


def parse_vehicle_info():
    info = {}
    vehicle_info_json = gm_api_post(vehicle_info)
    data = vehicle_info_json['data']
    color = data['color']['value']
    info["color"] = color
    drive_train = data['driveTrain']['value']
    info["driveTrain"] = drive_train
    vin = data['vin']['value']
    info["vin"] = vin
    if data['fourDoorSedan']['value'] == 'True':
        door_count = 4
    elif data['twoDoorCoupe']['value'] == 'True':
        door_count = 2
    else:
        door_count = None
    info["doorCount"] = door_count
    return info

print(parse_vehicle_info())
