from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import VehicleSerializer

import SmartCar as sc

from . models import Vehicle
from . models import Security
from . models import Fuel
from . models import Battery
from . models import Engine


# Create your views here.
id = 1234


def vehicle_info(request):
    info = sc.parse_vehicle_info(id)
    vehicle = Vehicle()
    vehicle.color = info['color']
    vehicle.door_count = info['doorCount']
    vehicle.vin = info['vin']
    vehicle.drive_train = info['driveTrain']
    vehicle.save()
    print(info)
    return HttpResponse("<H2> Vehicle info </H2>")


def security(request):
    print(sc.parse_security_info(id))
    return HttpResponse("<H2> Security </H2>")


def fuel(request):
    print(sc.parse_fuel_info(id))
    return HttpResponse("<H2> Fuel </H2>")


def battery(request):
    print(sc.parse_battery_info(id))
    return HttpResponse("<H2> Battery </H2>")


class VehicleList(APIView):
    def get(self, request):
        info = sc.parse_vehicle_info(id)
        vehicle = Vehicle()
        vehicle.color = info['color']
        vehicle.door_count = info['doorCount']
        vehicle.vin = info['vin']
        vehicle.drive_train = info['driveTrain']
        print(info)
        serializer = VehicleSerializer(vehicle)
        return Response(serializer.data)

    def post(self, request):
        pass