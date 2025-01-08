from django.shortcuts import render
from .models import Plants
from django.shortcuts import get_object_or_404


def house_plants_names(request):
    plant_names = Plants.objects.all()
    return render(request, 'my_plants/house_plants_names.html', {'names': plant_names})


def plant_detail(request, id):
    plant = get_object_or_404(Plants, id=id)
    return render(request, 'my_plants/plant_detail.html', {'plant': plant})