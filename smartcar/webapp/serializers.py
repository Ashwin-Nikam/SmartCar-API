from rest_framework import serializers
from . models import Vehicle
from . models import Security
from . models import Fuel
from . models import Battery
from . models import Engine


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('vin', 'color', 'door_count', 'drive_train')
