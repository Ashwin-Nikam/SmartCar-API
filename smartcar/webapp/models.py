from django.db import models

# Create your models here.


class Vehicle(models.Model):
    vin = models.CharField(max_length=50, default="", primary_key=True)
    color = models.CharField(max_length=50, default="")
    doorCount = models.IntegerField(default=1)
    driveTrain = models.CharField(max_length=50, default="")


class Security(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, default="")
    location = models.CharField(max_length=50, default="")
    locked = models.BooleanField(default=True)


class Fuel(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, default="")
    percent = models.CharField(max_length=50, default="")


class Battery(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, default="")
    percent = models.CharField(max_length=50, default="")


class Engine(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, default="")
    status = models.CharField(max_length=50, default="")
