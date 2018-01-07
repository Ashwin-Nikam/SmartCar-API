from django.db import models

# Create your models here.


class Vehicle(models.Model):
    vin = models.CharField(max_length=50, default="")
    color = models.CharField(max_length=50, default="")
    doorCount = models.IntegerField(default=1)
    driveTrain = models.CharField(max_length=50, default="")


class Security(models.Model):
    location = models.CharField(max_length=50, default="")
    locked = models.BooleanField(default=True)


class Fuel(models.Model):
    percent = models.CharField(max_length=50, default="")


class Battery(models.Model):
    percent = models.CharField(max_length=50, default="")


class Engine(models.Model):
    status = models.CharField(max_length=50, default="")
