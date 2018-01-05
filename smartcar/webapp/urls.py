from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^vehicles/\d{4}', views.index, name='index')
]