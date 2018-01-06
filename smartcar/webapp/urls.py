from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^vehicles/\d{4}$', views.VehicleInfo.as_view()),
    url(r'^vehicles/\d{4}/doors', views.SecurityInfo.as_view()),
    url(r'^vehicles/\d{4}/fuel', views.FuelInfo.as_view()),
    url(r'^vehicles/\d{4}/battery', views.BatteryInfo.as_view())
]