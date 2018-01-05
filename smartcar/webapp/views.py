from django.http import HttpResponse

# Create your views here.


def index(request):
    print(request)
    return HttpResponse("<H2> Hello world </H2>")
