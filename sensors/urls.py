from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
  url(r'^$', TemplateView.as_view(template_name="index.html"), name='index'),
  url(r'^sensor/(\d+)/([-+]?\d*\.*\d+)/([-+]?\d*\.*\d+)/([-+]?\d*\.*\d+)/([-+]?\d*\.*\d+)/?$', views.sensor), #sensorid/humidity/pressure/temp/light
  url(r'^ui/?$', views.ui),
  url(r'^clear/?$', views.clear),
]
