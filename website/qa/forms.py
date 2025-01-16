from django import forms
from .models import Question, Answer


class AskingQuestion(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'detail', 'topic']


class QuestionEdit(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'detail', 'topic']


class SaveAnswer(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['detail']


class SearchQuestions(forms.Form):
    query = forms.CharField(max_length=100, widget=forms.TextInput({'placeholder' : "جستوجو"}))
