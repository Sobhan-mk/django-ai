from django.urls import path
from .views import ask_question, edit_question

app_name = 'qa'
urlpatterns = [
    path('ask_question/', ask_question, name='ask_questions'),
    path('edit_question/<int:id>', edit_question, name='edit_question')

]