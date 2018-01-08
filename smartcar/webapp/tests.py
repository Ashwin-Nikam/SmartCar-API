"""
Testing
15 tests have been written for testing the SmartCar API organized into 3 main classes

1. GeneralMotorsUtilityTests : Tests for checking whether the GM API responds correctly
                               to requests

2. SmartCarUtilityTests:       Tests for checking functionality of all the methods in
                               utilities/SmartCar.py

3. SmartCarApiTests:           Tests for checking whether the SmartCar API responds
                               correctly to requests
"""


import json

import requests
from django.test import TestCase

from webapp.utilities import GeneralMotors as gm, SmartCar as sc

# Create your tests here.

ids = [1234, 1235]


class GeneralMotorsUtilityTests(TestCase):
    # Testing the status code in the response from GM API
    def test_vehicle_info(self):
        service = sc.vehicle_info
        for id in ids:
            response = gm.post_request(service, id, None, None)
            self.assertEquals(response['status'], '200')
            color = response['data']['color']['value']
            if id == 1234:
                self.assertEquals(color, 'Metallic Silver')
            elif id == 1235:
                self.assertEquals(color, 'Forest Green')

    def test_security(self):
        service = sc.security
        for id in ids:
            response = gm.post_request(service, id, None, None)
            self.assertEquals(response['status'], '200')

    def test_fuel_battery(self):
        service = sc.energy_level
        for id in ids:
            response = gm.post_request(service, id, None, None)
            self.assertEquals(response['status'], '200')

    def test_engine(self):
        service = sc.engine
        actions = ["START", "STOP"]
        for id in ids:
            for action in actions:
                response = gm.post_request(service, id, None, action)
                self.assertEquals(response['status'], '200')


class SmartCarUtilityTests(TestCase):
    def test_vehicle_info(self):
        for id in ids:
            response = sc.get_vehicle_info(id)
            self.assertNotEqual(response, 'Status code other than 200 received!')
            if id == 1234:
                self.assertEquals(response['vin'], '123123412412')
                self.assertEquals(response['color'], 'Metallic Silver')
                self.assertEquals(response['doorCount'], 4)
                self.assertEquals(response['driveTrain'], 'v8')
            elif id == 1235:
                self.assertEquals(response['vin'], '1235AZ91XP')
                self.assertEquals(response['color'], 'Forest Green')
                self.assertEquals(response['doorCount'], 2)
                self.assertEquals(response['driveTrain'], 'electric')

    def test_security(self):
        for id in ids:
            response = sc.get_security(id)
            self.assertNotEqual(response, 'Status code other than 200 received!')

    def test_fuel_battery(self):
        for id in ids:
            response1 = sc.get_fuel(id)
            response2 = sc.get_battery(id)
            self.assertNotEqual(response1, 'Status code other than 200 received!')
            self.assertNotEqual(response2, 'Status code other than 200 received!')

    def test_engine(self):
        for id in ids:
            content_type = 'application/json'
            actions = ['START', 'STOP']
            for action in actions:
                response = sc.get_engine(id, content_type, action)
                self.assertNotEqual(response, 'Status code other than 200 received!')

    # Testing whether the API provides response with status code other than 200 for fake Vehicle Id 1236
    def test_non_working_id(self):
        response = sc.get_vehicle_info(1236)
        self.assertEquals(response, 'Status code other than 200 received!')


class SmartCarApiTests(TestCase):

    BASE_URL = 'http://localhost:8000/vehicles/'

    # Testing the status code in the response from SmartCar API
    def test_vehicle_info(self):
        for id in ids:
            request_url = (SmartCarApiTests.BASE_URL + '%d') % id
            response = requests.get(request_url)
            self.assertEquals(response.status_code, 200)
            response = response.json()
            if id == 1234:
                self.assertEquals(response['vin'], '123123412412')
                self.assertEquals(response['color'], 'Metallic Silver')
                self.assertEquals(response['doorCount'], 4)
                self.assertEquals(response['driveTrain'], 'v8')
            elif id == 1235:
                self.assertEquals(response['vin'], '1235AZ91XP')
                self.assertEquals(response['color'], 'Forest Green')
                self.assertEquals(response['doorCount'], 2)
                self.assertEquals(response['driveTrain'], 'electric')

    def test_security(self):
        for id in ids:
            request_url = (SmartCarApiTests.BASE_URL + '%d/doors') % id
            response = requests.get(request_url)
            self.assertEquals(response.status_code, 200)

    def test_fuel(self):
        for id in ids:
            request_url = (SmartCarApiTests.BASE_URL + '%d/fuel') % id
            response = requests.get(request_url)
            self.assertEquals(response.status_code, 200)

    def test_battery(self):
        for id in ids:
            request_url = (SmartCarApiTests.BASE_URL + '%d/battery') % id
            response = requests.get(request_url)
            self.assertEquals(response.status_code, 200)

    def test_engine(self):
        headers = {'Content-Type': 'application/json'}
        actions = ["START", "STOP"]
        for id in ids:
            request_url = (SmartCarApiTests.BASE_URL + '%d/engine') % id
            for action in actions:
                payload = {"action": action}
                response = requests.post(request_url, headers=headers, data=json.dumps(payload))
                self.assertEquals(response.status_code, 200)

    # Testing whether the response from  API provides status code other than 200 for fake Vehicle Id 1236
    def test_non_working_case(self):
        request_url = (SmartCarApiTests.BASE_URL + '%d') % 1236
        response = requests.get(request_url)
        self.assertNotEqual(response.status_code, 200)