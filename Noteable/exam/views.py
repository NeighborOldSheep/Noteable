from django.shortcuts import render
from exam.models import *
from django.views.generic import ListView, TemplateView 
from course.models import *
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"exam/index.html")
    

def psycology_test(request):
    psychology_test = Question.objects.filter(subject__contains="psychology")
    print(psychology_test)
    return render(request,'exam/psychology_exam.html',{'psychology_test':psychology_test})

def world_history_test(request):
    world_history_test = Question.objects.filter(subject__contains="world history")
    print(world_history_test)
    return render(request,'exam/world_hisotry_exam.html',{'world_history_test':world_history_test})

  