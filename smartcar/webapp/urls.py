from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^vehicles/\d{4}$', views.VehicleList.as_view()),
    url(r'^vehicles/\d{4}/doors', views.security),
    url(r'^vehicles/\d{4}/fuel', views.fuel),
    url(r'^vehicles/\d{4}/battery', views.battery)
]