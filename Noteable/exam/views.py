from django.shortcuts import render
from exam.models import *
from django.views.generic import ListView, TemplateView 
from course.models import *
from django.http import HttpResponse
from django.template.defaultfilters import striptags #去掉富文本的html标签
import re

# Create your views here.
def index(request):
    return render(request,"exam/index.html")
    

def psycology_test(request):
    psychology_test = Question.objects.filter(subject__contains="psychology")
    #print(psychology_test)
    return render(request,'exam/psychology_exam.html',{'psychology_test':psychology_test})

def world_history_test(request):
    world_history_test = Question.objects.filter(subject__contains="world history")
    #print(world_history_test)
    return render(request,'exam/world_hisotry_exam.html',{'world_history_test':world_history_test})


def macro_economic_test(request):
    macro_economic_test = Question.objects.filter(subject__contains="marco")
    #print(world_history_test)
    return render(request,'exam/marco_economic_exam.html',{'macro_economic_test':macro_economic_test})


def physics_A_test(request):
    physics_A_test = Question.objects.filter(subject__contains="physicsA")
    
    
    """ physics_A_test = striptags(physics_A_tests)
    print(physics_A_test) """
    

    return render(request,'exam/physics_A_exam.html',{'physics_A_test':physics_A_test})
  