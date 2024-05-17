from django.http import HttpResponse
from django.shortcuts import render
from polls.models import Question, Answer

# Create your views here.

def index(request):
    questions = Question.objects.order_by("-date")
    context = {
        "questions": questions,
    }
    return render(request, "index.html", context)

def detail(request, question_id):
    return HttpResponse(f"You're looking at question number: {question_id}")