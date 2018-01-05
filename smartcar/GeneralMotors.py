import SmartCar as sc
import requests
import json

BASE_URL = 'http://gmapi.azurewebsites.net'


def post_request(service, id, content_type, action):
    request_url = BASE_URL + service
    if service == sc.engine:
        if action == '"START"':
            payload = {'id': id, 'command': "START_VEHICLE",
                       'responseType': 'JSON'}
        elif action == '"STOP"':
            payload = {'id': id, 'command': "STOP_VEHICLE",
                       'responseType': 'JSON'}
        else:
            return "Invalid input"
    else:
        payload = {'id': id, 'responseType': 'JSON'}
    if content_type is not None:
        headers = {'Content-Type': content_type}
    else:
        headers = {'Content-Type': 'application/json'}
    response = requests.post(request_url, headers=headers, data=json.dumps(payload)).json()
    return response
