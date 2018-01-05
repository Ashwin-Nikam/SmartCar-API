from django.db import models

# Create your models here.


class Vehicle(models.Model):
    vin = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    door_count = models.IntegerField()
    drive_train = models.CharField(max_length=50)


class Security(models.Model):
    location = models.CharField(max_length=50)
    locked = models.BooleanField()


class Fuel(models.Model):
    percent = models.FloatField()


class Battery(models.Model):
    percent = models.FloatField()


class Engine(models.Model):
    status = models.CharField(max_length=50)