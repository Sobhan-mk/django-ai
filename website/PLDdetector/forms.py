from django.contrib.auth.forms import forms
from .models import PlantLeaf


class PlantLeafForm(forms.ModelForm):
    class Meta:
        model = PlantLeaf
        fields = ['image']
        widgets = {'image': forms.ClearableFileInput(attrs={'class': 'form-control'}), }
        labels = {'image': '', }