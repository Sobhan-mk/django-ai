from django.contrib.auth.urls import path
from . import views

app_name = 'PLDdetector'
urlpatterns = [
    path('detector_model/', views.detector_model, name='detector_model')
]