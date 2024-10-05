from django.shortcuts import render, redirect
from .forms import UserCreateForm, UserRegisterForm
from .models import UserManager
from .models import User


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
    return render(request, 'accounts/login.html')