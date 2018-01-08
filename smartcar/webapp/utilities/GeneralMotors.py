"""
Main API call to the General Motors API
post_request() : calls the General Motors API and returns the response in json format.
post_request() has 4 parameters

1. service:      Determines which POST request has to be made (eg: /getVehicleInfoService,
                 /getEnergyService etc)

2. id:           Vehicle Id (eg: 1234, 1235 etc)

3. content_type: The MIME type of the content (eg: application/json)

4. action:       This parameter is only required when the service is /actionEngineService
                 for determining whether to START/STOP engine. It is set to None otherwise.
"""

import json

import requests

from webapp.utilities import SmartCar as sc

BASE_URL = 'http://gmapi.azurewebsites.net'


def post_request(service, id, content_type, action):
    request_url = BASE_URL + service
    if service == sc.engine:
        if action == 'START':
            payload = {'id': id, 'command': "START_VEHICLE",
                       'responseType': 'JSON'}
        elif action == 'STOP':
            payload = {'id': id, 'command': "STOP_VEHICLE",
                       'responseType': 'JSON'}
    else:
        payload = {'id': id, 'responseType': 'JSON'}
    if content_type is not None:
        headers = {'Content-Type': content_type}
    else:
        headers = {'Content-Type': 'application/json'}
    response = requests.post(request_url, headers=headers, data=json.dumps(payload)).json()
    return response
