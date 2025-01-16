from django.shortcuts import render, redirect
from .forms import AskingQuestion, QuestionEdit, SaveAnswer, SearchQuestions
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .models import Question, Answer
from django.db.models import Prefetch
import random
from django.db.models import Q


def external_qa_page(request):

    query = request.GET.get('query')

    search_form = SearchQuestions()

    if query:
        question_ids = list(Question.objects.filter(
            Q(title__icontains=query) |
            Q(detail__icontains=query) |
            Q(topic__icontains=query)
        ).values_list('id', flat=True))
    else:
        question_ids = list(Question.objects.values_list('id', flat=True))

    # Randomly sample 10 question IDs
    random_question_ids = random.sample(question_ids, min(len(question_ids), 10))

    # Get questions and prefetch related answers
    questions_with_answers = Question.objects.filter(id__in=random_question_ids).prefetch_related(
        Prefetch('answers', queryset=Answer.objects.all()))

    return render(request, 'qa/external_question_page.html', {'questions_with_answers': questions_with_answers, 'search_form' : search_form})


def search_questions(request):
    query = request.GET.get('q')
    if query:
        results = Question.objects.filter(
            Q(question_text__icontains=query) |
            Q(topic__icontains=query) |
            Q(custom_topic__icontains=query)
        )
    else:
        results = Question.objects.all()
    return render(request, 'qa/external_question_page.html', {'results': results})



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


def show_answers(request, id):
    question = Question.objects.get(id=id)
    answers = question.answer.all()

    return render(request, 'qa/answers.html', {'answers' : answers})


def save_answer(request, id):
    question = Question.objects.get(id=id)

    if request.method == 'POST':
        form = SaveAnswer(request.POST)

        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.user = request.user

            answer.save()

            messages.success(request, 'پاسخ شما با موفقیت ثبت شد.')
            return redirect('home:home')

    else:
        form = SaveAnswer()

    return render(request, 'qa/save_answer.html', {'form': form})
