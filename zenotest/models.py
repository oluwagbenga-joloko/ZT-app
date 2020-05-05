from django.db import models

# Create your models here.

# id,timestamp,temperature,duration

class TempMeasurement(models.Model):
    # id = models.AutoField()
    timestamp = models.DateTimeField(null=True)
    temperature = models.FloatField(null=True)
    duration = models.DurationField(null=True)
    created = models.DateTimeField(auto_now_add=True)

class Logs(models.Model):
    method = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
