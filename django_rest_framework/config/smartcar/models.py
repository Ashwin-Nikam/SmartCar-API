from django.db import models

# Create your models here.


class Vehicles(models.Model):
    vin = models.IntegerField()
    color = models.CharField(max_length=50)
    door_count = models.IntegerField()
    drive_train = models.CharField(max_length=50)

    def __str__(self):
        return self.color
