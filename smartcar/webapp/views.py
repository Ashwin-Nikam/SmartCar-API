from django.http import HttpResponse
import SmartCar as sc

# Create your views here.


def vehicle_info(request):
    print(type(request))
    print(sc.parse_vehicle_info(1234))
    return HttpResponse("<H2> Vehicle info </H2>")


def security(request):
    print(sc.parse_security_info(1234))
    return HttpResponse("<H2> Security </H2>")


def fuel(request):
    print(sc.parse_fuel_info(1234))
    return HttpResponse("<H2> Fuel </H2>")


def battery(request):
    print(sc.parse_battery_info(1234))
    return HttpResponse("<H2> Battery </H2>")