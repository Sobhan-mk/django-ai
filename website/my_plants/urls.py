from django.contrib.auth.urls import path
from . import views


app_name = 'my_plants'
urlpatterns = [
    path('house plants names/', views.house_plants_names, name='house_plants_names'),
    path('house plants names/<int:id>/', views.plant_detail, name='plant_detail'),
    path('plant_adder/<int:plant_id>/', views.user_plant_adder, name='user_plant_adder'),
]