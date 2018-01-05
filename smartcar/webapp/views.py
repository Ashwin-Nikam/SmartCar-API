from django.http import HttpResponse
from utilities import GeneralMotors
from utilities import SmartCar

# Create your views here.


def index(request):
    print(request)
    return HttpResponse("<H2> Hello world </H2>")
