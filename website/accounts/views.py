from django.shortcuts import render, redirect
from .forms import *
from .models import User, Profile
from django.contrib.auth import authenticate, login as dj_login, logout
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm

def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            User.objects.create_user(username=data['username'], email=data['email'], password=data['password_2'])

            messages.success(request, 'registration was sucessfully!', 'success')
            return redirect('home:home')
        
    else:
        form = UserRegisterForm()

    context = {'form':form}
    return render(request, 'accounts/register.html', context)


def login(request):
    error_message = None
    if request.method == 'POST':
        form = UserLoginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
           
            if not User.objects.filter(username=data['username']).exists():
                error_message = 'user not found'

            else:
                user = authenticate(request, username=data['username'], password=data['password'])
                if user is not None:
                    dj_login(request, user)

                    messages.success(request, 'login was sucessfully!', 'success')
                    
                    return redirect('home:home')
                else:
                    error_message = 'invalid username or password'
                
    else:
        form = UserLoginForm()

    context = {'form': form, 'error_message': error_message}

    return render(request, 'accounts/login.html', context)

def profile(request):
    if request.method == 'POST':

        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,
                                          request.FILES,
                                          instance=request.user.profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'profile updated secessfully!', 'success')

            return redirect('home:home')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
                                          
    profile = Profile.objects.get(user_id=request.user.id)

    context = {
        'profile' : profile,
        'user_form' : user_form, 
        'profile_form' : profile_form
    }

    return render(request, 'accounts/profile.html', context)


def signout(request):
    logout(request)
    messages.success(request, 'logout was secessfully!')
    return redirect('home:home')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'password changed succesfully!', 'success')
            return redirect('home:home')
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'accounts/change_password.html', {'form' : form})