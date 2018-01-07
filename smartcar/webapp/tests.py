from django.test import TestCase
import SmartCar as sc
import GeneralMotors as gm

# Create your tests here.


class TestBasic(TestCase):
    def test_basic(self):
        a = 1
        self.assertEqual(1, a)

    def test_basic_2(self):
        a = 1
        assert a == 1


class GeneralMotorsApiTest(TestCase):
    ids = [1234, 1235]

    def test_vehicle_info(self):
        service = sc.vehicle_info
        for id in GeneralMotorsApiTest.ids:
            response = gm.post_request(service, id, None, None)
            self.assertEquals(response['status'], '200')

    def test_vehicle_info(self):
        service = sc.vehicle_info
        for id in GeneralMotorsApiTest.ids:
            response = gm.post_request(service, id, None, None)
            self.assertEquals(response['status'], '200')