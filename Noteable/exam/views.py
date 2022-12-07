from django.shortcuts import render
from exam.models import *
from django.views.generic import ListView, TemplateView

# Create your views here.
class IndexView(ListView):
    template_name = 'exam\index.html'
    model = Subject