from django.db import models

# Create your models here.


class Vehicle(models.Model):
    vin = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    door_count = models.IntegerField()
    drive_train = models.CharField(max_length=50)
    main_id = models.CharField(primary_key=True, max_length=50)


class Security(models.Model):
    vehicle = models.ForeignKey(Vehicle)
    location = models.CharField(max_length=50)
    locked = models.BooleanField()


class Fuel(models.Model):
    vehicle = models.ForeignKey(Vehicle)
    percent = models.FloatField()


class Battery(models.Model):
    vehicle = models.ForeignKey(Vehicle)
    percent = models.FloatField()


class Engine(models.Model):
    vehicle = models.ForeignKey(Vehicle)
    status = models.CharField(max_length=50)
