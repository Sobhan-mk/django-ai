from django.shortcuts import render, redirect
from .forms import *
from .models import User, Profile
from django.contrib.auth import authenticate, login as dj_login, logout
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash


def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            User.objects.create_user(username=data['username'], email=data['email'], password=data['password_2'])

            messages.success(request, 'حساب کاربری شما ساخته شد', 'success')
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

                    messages.success(request, 'ورود موفقیت آمیر بود', 'success')
                    
                    return redirect('home:home')
                else:
                    error_message = 'نام کاربری یا روز عبور اشتباه است'
                
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
            messages.success(request, 'پروفایل بروز رسانی شد', 'success')

            return redirect('home:home')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    profile = Profile.objects.get(user_id=request.user.id)


    user_plants = profile.users_plants.all()

    user_questions = request.user.questions.all()



    context = {
        'profile' : profile,
        'user_form' : user_form, 
        'profile_form' : profile_form,
        'user_plants' : user_plants,
        'user_questions' : user_questions
    }

    return render(request, 'accounts/profile.html', context)


def signout(request):
    logout(request)
    messages.success(request, 'شما خارج شدید')
    return redirect('home:home')


def change_password(request):
    error = ''
    if request.method == 'POST':
        form = ChangePassword(data=request.POST)

        if form.is_valid():
            old_password = form.cleaned_data['old_password']
            new_password = form.cleaned_data['new_password']
            repeat_password = form.cleaned_data['repeat_password']
            if request.user.check_password(old_password):
                if new_password == repeat_password:
                    request.user.set_password(new_password)
                    request.user.save()

                    update_session_auth_hash(request, request.user)

                    messages.success(request, 'رمز عبور شما با موفقیت تغییر کرد')
                    return redirect('accounts:profile')

                else:
                    error = 'رمز عبور جدید با تکرار آن مطابقت ندارد'
            else:
                error = 'رمز عبور قمیمی شما درست نیست'

    else:
        form = ChangePassword()

    context = {
        'form': form,
        'error': error
    }

    return render(request, 'accounts/change_password.html', context)