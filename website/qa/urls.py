from django.urls import path
from .views import external_qa_page, ask_question, edit_question, show_answers, save_answer

app_name = 'qa'
urlpatterns = [
    path('search/', external_qa_page, name='external_qa_page'),
    path('ask_question/', ask_question, name='ask_questions'),
    path('edit_question/<int:id>', edit_question, name='edit_question'),
    path('show_answers/<int:id>', show_answers, name='show_answers'),
    path('answer/<int:id>', save_answer, name='save_answer')

]