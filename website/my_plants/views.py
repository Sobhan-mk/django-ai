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
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, user=request.user)
        user_plants = profile.users_plants.all()

        context = {'plant' : plant, 'user_plants' : user_plants}
    else:
        context = {'plant': plant}
    return render(request, 'my_plants/plant_detail.html', context)


def user_plant_adder(request, plant_id):

    plant = get_object_or_404(Plants, id=plant_id)
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, user=request.user)

        profile.users_plants.add(plant)
        profile.save()

        messages.success(request, f'{plant.name} به گیاهان شما اضافه شد.', "success")
        return redirect('my_plants:house_plants_names')
    else:
        return redirect('accounts:login')


def user_plant_remover(request, plant_id):
    plant = get_object_or_404(Plants, id=plant_id)
    profile = get_object_or_404(Profile, user=request.user)

    messages.success(request, f'{plant.name} از گیاهان شما حذف شد', "success")

    profile.users_plants.remove(plant)
    return redirect('my_plants:house_plants_names')


def user_plant_remover_all(request):
    profile = get_object_or_404(Profile, user=request.user)

    messages.success(request, 'تمام گیاهان حذف شدند ', "success")

    profile.users_plants.clear()
    return redirect('my_plants:house_plants_names')
