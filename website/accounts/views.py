from django.shortcuts import render, redirect
from .forms import *
from .models import UserManager
from .models import User
from django.contrib.auth import authenticate, login as dj_login


def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            User.objects.create_user(username=data['username'], email=data['email'], phone=data['phone'], password=data['password_2'])

            return redirect('home:home')
        
    else:
        form = UserRegisterForm()

    context = {'form':form}
    return render(request, 'accounts/register.html', context)


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            user = authenticate(request, username=data['username'], password=data['password'])
           
            if user is not None:
                dj_login(request, user)
                return redirect('home:home')
            
            else:
                pass
    else:
        form = UserLoginForm()

    context = {'form' : form}

    return render(request, 'accounts/login.html', context)