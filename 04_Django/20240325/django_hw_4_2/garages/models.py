from django.db import models

# Create your models here.
class Garage(models.Model):
    id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=200)
    capacity = models.IntegerField()
    is_parking_available = models.BooleanField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()