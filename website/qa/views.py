from django.shortcuts import render, redirect
from .forms import AskingQuestion, QuestionEdit
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .models import Question


def ask_question(request):
    if request.method == 'POST':
        form = AskingQuestion(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()

            messages.success(request,'شوال شما با موفقیت ثبت شد.')
            return redirect('home:home')
    else:
        form = AskingQuestion()
    return render(request, 'qa/ask_question.html', {'form': form})


def edit_question(request, id):
    question = get_object_or_404(Question, id=id)
    if request.method == 'POST':
        form = QuestionEdit(request.POST, instance=question)

        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()

            return redirect('home:home')

    else:
        form = QuestionEdit(instance=question)
    context = {'form': form, 'question_title' : question.title}

    return render(request, 'qa/edit_question.html', context)


