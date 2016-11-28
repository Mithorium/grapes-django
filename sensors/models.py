from __future__ import unicode_literals

from django.db import models
import json
import time

# Create your models here.

class Sensor(models.Model):
  sensor_id = models.IntegerField(primary_key=True)
  last_update = models.DateTimeField(auto_now=True)
  humidity = models.DecimalField(max_digits=10, decimal_places=3)
  pressure = models.DecimalField(max_digits=10, decimal_places=3)
  temperature = models.DecimalField(max_digits=10, decimal_places=3)
  light = models.DecimalField(max_digits=10, decimal_places=3)
  min_humidity = models.DecimalField(max_digits=10, decimal_places=3)
  max_humidity = models.DecimalField(max_digits=10, decimal_places=3)
  avg_humidity = models.DecimalField(max_digits=10, decimal_places=3)
  min_pressure = models.DecimalField(max_digits=10, decimal_places=3)
  max_pressure = models.DecimalField(max_digits=10, decimal_places=3)
  avg_pressure = models.DecimalField(max_digits=10, decimal_places=3)
  min_temp = models.DecimalField(max_digits=10, decimal_places=3)
  max_temp = models.DecimalField(max_digits=10, decimal_places=3)
  avg_temp = models.DecimalField(max_digits=10, decimal_places=3)
  color = models.CharField(max_length=6)
  
  def getObj(self):
    obj = {}
    obj['id'] = self.sensor_id
    obj['updated'] = time.mktime(self.last_update.timetuple())
    obj['humidity'] = {'current': self.humidity, 'min': self.min_humidity, 'max': self.max_humidity, 'avg': self.avg_humidity}
    obj['pressure'] = {'current': self.pressure, 'min': self.min_pressure, 'max': self.max_pressure, 'avg': self.avg_pressure}
    obj['temperature'] = {'current': self.temperature, 'min': self.min_temp, 'max': self.max_temp, 'avg': self.avg_temp}
    obj['light'] = self.light
    obj['color'] = self.color
    return obj

  def __str__(self):
    return str(self.sensor_id)
