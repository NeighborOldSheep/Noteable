from django.shortcuts import render
from .models import Psychology,Economics,Env_science,Human_Geography,World_history,Seminar
from django.views.generic import ListView, DetailView

# Create your views here.
def course(request):
    return render(request,"course/course.html")

#Psychology
def psychology(request):
    psychology = Psychology.objects.all()
    context = {"psychology":psychology}

    return render(request,'course/psychology.html',context)

""" class PsychologyNotes(DetailView):
    model = Psychology
    template_name = 'course/psychology_notes.html'
    context_object_name = psychology """
def psychology_notes(request,id):
    psychology = Psychology.objects.get(id=id)
    dict_psychology = {}
    
    #save each of the chapter name
    dict_psychology['chapter'] = psychology.title
    #save each chapter notes
    dict_psychology['notes'] = psychology.notes
    
    return render(request,'course/psychology_notes.html',dict_psychology)

#Human-Geography
def human_geography(request):
    ob = Human_Geography.objects.all()
    context = {"psychology":ob}

    return render(request,'course/human_geography.html')

#economics
def economics(request):
    ob = Economics.objects.all()
    context = {"psychology":ob}
    return render(request,'course/economics.html')

#env-science
def env_science(request):
    ob = Env_science.objects.all()
    context = {"psychology":ob}
    return render(request,'course/env_science.html')

#world-history
def world_history(request):
    ob = World_history.objects.all()
    context = {"psychology":ob}
    return render(request,'course/world_history.html')

#seminar
def seminar(request):
    ob = Seminar.objects.all()
    context = {"psychology":ob}
    return render(request,'course/seminar.html')