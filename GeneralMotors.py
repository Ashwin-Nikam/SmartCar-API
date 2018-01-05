import requests
import json
import SmartCar as sc

BASE_URL = 'http://gmapi.azurewebsites.net'


def post_request(service, id):
    request_url = BASE_URL + service
    if service == sc.engine:
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
