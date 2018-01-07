from django.test import TestCase
import SmartCar as sc
import GeneralMotors as gm

# Create your tests here.


class GeneralMotorsApiTest(TestCase):
    ids = [1234, 1235]

    def test_vehicle_info(self):
        service = sc.vehicle_info
        for id in GeneralMotorsApiTest.ids:
            response = gm.post_request(service, id, None, None)
            self.assertEquals(response['status'], '200')
            color = response['data']['color']['value']
            if id == 1234:
                self.assertEquals(color, 'Metallic Silver')
            elif id == 1235:
                self.assertEquals(color, 'Forest Green')

    def test_security(self):
        service = sc.security
        for id in GeneralMotorsApiTest.ids:
            response = gm.post_request(service, id, None, None)
            self.assertEquals(response['status'], '200')

    def test_fuel_and_battery(self):
        service = sc.energy_level
        for id in GeneralMotorsApiTest.ids:
            response = gm.post_request(service, id, None, None)
            self.assertEquals(response['status'], '200')

    def test_start_stop(self):
        service = sc.engine
        commands = ["START", "STOP"]
        for id in GeneralMotorsApiTest.ids:
            for command in commands:
                response = gm.post_request(service, id, None, command)
                self.assertEquals(response['status'], '200')
