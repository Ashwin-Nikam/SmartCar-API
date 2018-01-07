"""smartcar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from webapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'vehicles/(?P<id>\d{4})$', views.VehicleInfo.as_view()),
    url(r'vehicles/(?P<id>\d{4})/doors$', views.SecurityInfo.as_view()),
    url(r'vehicles/(?P<id>\d{4})/fuel$', views.FuelInfo.as_view()),
    url(r'vehicles/(?P<id>\d{4})/battery$', views.BatteryInfo.as_view()),
    url(r'vehicles/(?P<id>\d{4})/engine$', views.Engine.as_view()),
    url(r'^$', views.home)
]

urlpatterns = format_suffix_patterns(urlpatterns)
