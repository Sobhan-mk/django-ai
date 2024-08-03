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



        


    
    
