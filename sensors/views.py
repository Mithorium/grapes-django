from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from  django.views.decorators.gzip import gzip_page
import time
import json
from decimal import *
from sensors.models import Sensor

# Create your views here.


def index(request):
  return HttpResponse("Hello, world. You're at the sensors index.")

def sensor(request, sensorid, humidity, pressure, temperature, light):
  if Sensor.objects.filter(sensor_id=int(sensorid)):
    s = Sensor.objects.get(sensor_id=int(sensorid))
  else:
    s = Sensor(sensor_id=int(sensorid))
  
  humidity = Decimal(humidity)
  pressure = Decimal(pressure)
  temperature = Decimal(temperature)
  
  s.humidity = humidity
  s.pressure = pressure
  s.temperature = temperature
  s.light = Decimal(light)
  
  if s.min_humidity is None or humidity < s.min_humidity:
    s.min_humidity = humidity
  if s.max_humidity is None or humidity > s.max_humidity:
    s.max_humidity = humidity
  if s.avg_humidity is None:
    s.avg_humidity = humidity
  else:
    s.avg_humidity = s.avg_humidity * Decimal('0.8') + humidity * Decimal('0.2')
  
  if s.min_pressure is None or pressure < s.min_pressure:
    s.min_pressure = pressure
  if s.max_pressure is None or pressure > s.max_pressure:
    s.max_pressure = pressure
  if s.avg_pressure is None:
    s.avg_pressure = pressure
  else:
    s.avg_pressure = s.avg_pressure * Decimal('0.8') + pressure * Decimal('0.2')
    
  if s.min_temp is None or temperature < s.min_temp:
    s.min_temp = temperature
  if s.max_temp is None or temperature > s.max_temp:
    s.max_temp = temperature
  if s.avg_temp is None:
    s.avg_temp = temperature
  else:
    s.avg_temp = s.avg_temp * Decimal('0.8') + temperature * Decimal('0.2')
  
  if s.light > Decimal('0.9'):
    s.color = '5fb760'
  elif s.light > Decimal('0.4'):
    s.color = 'eeac57'
  else:
    s.color = 'd4564e'
  
  s.save()
  return JsonResponse(s.getObj())

@gzip_page
def ui(request):
  # response = JsonResponse([x.getObj() for x in Sensor.objects.all()], safe=False)
  # response['Access-Control-Allow-Origin'] = '*'
  # response['Access-Control-Allow-Headers'] = 'content-type'
  # return response
  return JsonResponse([x.getObj() for x in Sensor.objects.all()], safe=False)

def clear(request):
  Sensor.objects.all().delete()
  return HttpResponse("Sensors cleared")