from django.test import TestCase
import SmartCar as sc
import GeneralMotors as gm

# Create your tests here.

ids = [1234, 1235]


class GeneralMotorsApiTest(TestCase):
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

    def test_start_stop(self):
        service = sc.engine
        actions = ["START", "STOP"]
        for id in ids:
            for action in actions:
                response = gm.post_request(service, id, None, action)
                self.assertEquals(response['status'], '200')


class SmartCarApiTest(TestCase):
    def test_vehicle_info(self):
        for id in ids:
            response = sc.parse_vehicle_info(id)
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
            response = sc.parse_security_info(id)
            self.assertNotEqual(response, 'Status code other than 200 received!')

    def test_fuel_battery(self):
        for id in ids:
            response1 = sc.parse_fuel_info(id)
            response2 = sc.parse_battery_info(id)
            self.assertNotEqual(response1, 'Status code other than 200 received!')
            self.assertNotEqual(response2, 'Status code other than 200 received!')

    def test_start_stop(self):
        for id in ids:
            content_type = 'application/json'
            actions = ['START', 'STOP']
            for action in actions:
                response = sc.start_stop_engine(id, content_type, action)
                self.assertNotEqual(response, 'Status code other than 200 received!')

    def test_non_working_id(self):
        response = sc.parse_vehicle_info(1236)
        self.assertEquals(response, 'Status code other than 200 received!')

