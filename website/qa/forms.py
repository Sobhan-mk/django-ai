from django import forms
from .models import Question


class AskingQuestion(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'detail']


class QuestionEdit(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'detail']
