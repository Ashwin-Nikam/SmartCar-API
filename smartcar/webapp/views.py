from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request
from .serializers import VehicleSerializer
from .serializers import SecuritySerializer
from .serializers import BatterySerializer
from .serializers import FuelSerializer
from .serializers import EngineSerializer
from rest_framework.decorators import api_view

import SmartCar as sc

from . models import Vehicle
from . models import Security
from . models import Fuel
from . models import Battery
from . models import Engine


# Create your views here.


class VehicleInfo(APIView):
    def get(self, request, id):
        info = sc.parse_vehicle_info(id)
        vehicle = Vehicle()
        vehicle.color = info['color']
        vehicle.door_count = info['doorCount']
        vehicle.vin = info['vin']
        vehicle.drive_train = info['driveTrain']
        serializer = VehicleSerializer(vehicle)
        return Response(serializer.data)

    def post(self):
        pass


class SecurityInfo(APIView):
    def get(self, request, id):
        info = sc.parse_security_info(id)
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
        info = sc.parse_fuel_info(id)
        fuel = Fuel()
        fuel.percent = info['percent']
        serializer = FuelSerializer(fuel)
        return Response(serializer.data)

    def post(self):
        pass


class BatteryInfo(APIView):
    def get(self, request, id):
        info = sc.parse_battery_info(id)
        battery = Battery()
        battery.percent = info['percent']
        serializer = BatterySerializer(battery)
        return Response(serializer.data)

    def post(self):
        pass


class Engine(APIView):
    main_id = None

    def get(self, request, id):
        Engine.main_id = id
        return Response()
        # return render(request, 'form.html')

    def post(self, request, id):
        print(id)
        print(request.content_type)
        print(request.data)
        return Response()

    @api_view(['GET', 'POST', ])
    def create(request):
        action = request.POST['action']
        content_type = request.POST['content-type']
        info = sc.start_stop_engine(Engine.main_id, content_type, action)
        engine = Engine()
        engine.status = info['status']
        serializer = EngineSerializer(engine)
        return Response(serializer.data)
