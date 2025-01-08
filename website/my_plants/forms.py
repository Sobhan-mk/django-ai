from django import forms


class SearchPlantNames(forms.Form):
    query = forms.CharField(max_length=100, widget=forms.TextInput({'placeholder' : "جستوجو"}))