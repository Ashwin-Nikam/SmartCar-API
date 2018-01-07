from rest_framework import serializers
from . models import Vehicle
from . models import Security
from . models import Fuel
from . models import Battery
from . models import Engine


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['vin', 'color', 'doorCount', 'driveTrain']


class SecuritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Security
        fields = ['location', 'locked']


class FuelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fuel
        fields = ['percent']


class BatterySerializer(serializers.ModelSerializer):
    class Meta:
        model = Battery
        fields = ['percent']


class EngineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engine
        fields = ['status']

