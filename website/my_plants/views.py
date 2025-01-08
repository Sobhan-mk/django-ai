from django.shortcuts import render, redirect
from .models import Plants
from django.shortcuts import get_object_or_404
from .forms import SearchPlantNames
from accounts.models import Profile
from django.contrib import messages

def house_plants_names(request):
    plant_names = Plants.objects.all()
    form = SearchPlantNames()
    query = request.GET.get('query')

    if query:
        plant_names = plant_names.filter(name__icontains=query) | plant_names.filter(persian_name__icontains=query)

    return render(request, 'my_plants/house_plants_names.html', {'form': form, 'names': plant_names})


def plant_detail(request, id):
    plant = get_object_or_404(Plants, id=id)
    return render(request, 'my_plants/plant_detail.html', {'plant': plant})


def user_plant_adder(request, plant_id):

    plant = get_object_or_404(Plants, id=plant_id)
    profile = get_object_or_404(Profile, user=request.user)

    profile.users_plants.add(plant)
    profile.save()

    messages.success(request, f'{plant.name} added to your house plants', "success")
    return redirect('my_plants:house_plants_names')
