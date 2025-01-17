from django import forms
from .models import User, Profile
from django.contrib.auth.forms import ReadOnlyPasswordHashField as ROPHF
from django.contrib.auth.hashers import check_password
from django.contrib.auth.forms import PasswordChangeForm


class UserCreateForm(forms.ModelForm):
    pass_1 = forms.CharField(widget=forms.PasswordInput)
    pass_2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_pass_2(self):
        data = self.cleaned_data
        if data["pass_1"] and data["pass_2"] and data["pass_1"] != data["pass_2"]:
            raise forms.ValidationError('passwords dont match')
        return data["pass_2"]
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set(self.cleaned_data['pass_2'])
        if commit:
            user.save(using=self._db)

        return user
    

class UserChangeForm(forms.ModelForm):
    password = ROPHF

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_password(self):
        return self.initial['password']
    
        
class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'نام کاربری'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'ایمیل'}))

    password_1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور'}))
    password_2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'تکرار رمز عبور'}))


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'نام کاربری'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور'}))


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = []


class ChangePassword(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs = {'place_holder' : 'رمز عبور قدیمی'}))
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'place_holder': 'رمز عبور جدید'}))
    repeat_password = forms.CharField(widget=forms.PasswordInput(attrs = {'place_holder' : 'تکرار رمز عبور جدید'}))