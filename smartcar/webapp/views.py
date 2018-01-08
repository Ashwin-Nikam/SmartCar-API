"""
Views for the SmartCar API
Created views for each GET/POST request to the SmartCar API.
Whenever the SmartCar API is called, one of the following views
is triggered which calls the corresponding method in the
SmartCar.py file. The returned dictionary is used to create an
object of the model corresponding to the request. This object
is passed to the serializer to get the json response which is
then returned by the API.
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from .serializers import VehicleSerializer
from .serializers import SecuritySerializer
from .serializers import BatterySerializer
from .serializers import FuelSerializer
from .serializers import EngineSerializer
from . models import Vehicle
from . models import Security
from . models import Fuel
from . models import Battery
from . models import Engine
import SmartCar as sc


# Create your views here.

class VehicleInfo(APIView):
    def get(self, request, id):
        info = sc.get_vehicle_info(id)
        vehicle = Vehicle()
        vehicle.color = info['color']
        vehicle.doorCount = info['doorCount']
        vehicle.vin = info['vin']
        vehicle.driveTrain = info['driveTrain']
        serializer = VehicleSerializer(vehicle)
        return Response(serializer.data)

    def post(self):
        pass


class SecurityInfo(APIView):
    def get(self, request, id):
        info = sc.get_security(id)
        security_list = []
        for element in info:
            security = Security()
            security.location = element['location']
            security.locked = element['locked']
            security_list.append(security)
        serializer = SecuritySerializer(security_list, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class FuelInfo(APIView):
    def get(self, request, id):
        info = sc.get_fuel(id)
        fuel = Fuel()
        fuel.percent = info['percent']
        serializer = FuelSerializer(fuel)
        return Response(serializer.data)

    def post(self):
        pass


class BatteryInfo(APIView):
    def get(self, request, id):
        info = sc.get_battery(id)
        battery = Battery()
        battery.percent = info['percent']
        serializer = BatterySerializer(battery)
        return Response(serializer.data)

    def post(self):
        pass


class Engine(APIView):
    def get(self, request, id):
        return Response()

    def post(self, request, id):
        content_type = request.content_type
        action = request.data['action']
        info = sc.get_engine(id, content_type, action)
        engine = Engine()
        engine.status = info['status']
        serializer = EngineSerializer(engine)
        return Response(serializer.data)


def home(request):
    return render(request, 'index.html')