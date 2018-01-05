from django.http import HttpResponse
import GeneralMotors as gm
import SmartCar as sc
# Create your views here.


def vehicle_info(request):
    print(type(request))
    print(sc.parse_vehicle_info(1234))
    return HttpResponse("<H2> Hello world </H2>")
