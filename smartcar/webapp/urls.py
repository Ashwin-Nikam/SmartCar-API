from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^vehicles/\d{4}$', views.VehicleList.as_view()),
    url(r'^vehicles/\d{4}/doors', views.SecurityList.as_view()),
    url(r'^vehicles/\d{4}/fuel', views.FuelList.as_view()),
    url(r'^vehicles/\d{4}/battery', views.BatteryList.as_view())
]