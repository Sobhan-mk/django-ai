from django import forms
from .models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField as ROPHF


class UserCreateForm(forms.ModelForm):
    pass_1 = forms.CharField(widget=forms.PasswordInput)
    pass_2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone']

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
        fields = ['username', 'email', 'phone']

    def clean_password(self):
        return self.initial['password']
    
        
class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField()
    phone = forms.IntegerField()

    password_1 = forms.CharField()
    password_2 = forms.CharField()

    def clean_username(self):
        user = self.cleaned_data['username']

        if User.objects.filter(username=user).exists():
            raise forms.ValidationError('username is already exist.')
        else:
            return user
        
    def clean_email(self):
        email = self.cleaned_data['email']

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('email is already exist')
        else:
            return email
        
    def clean_password_2(self):
        pass_1 = self.cleaned_data['password_1']
        pass_2 = self.cleaned_data['password_2']

        if pass_1 != pass_2:
            raise forms.ValidationError('passwords dont match')
        
        elif len(pass_2) < 10:
            raise forms.ValidationError('password is too short')
        
        elif not any (i.isupper() for i in pass_2):
            raise forms.ValidationError('pleas entre an upper alphabet in your password')
        
        else:
            return pass_1


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()