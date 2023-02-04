from django.shortcuts import render
from .models import Psychology,Macroeconomics,Env_science,Human_Geography,World_history,US_hisotry
from django.views.generic import ListView, DetailView
import markdown

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
    
    psychology.notes = markdown.markdown(psychology.notes,
    extension = [
        #包含缩进、表格等常用扩展
        'markdown.extensison.extra',
        #语法高亮扩展
        'markdown.extensions.codehilite'
    ])

    #save each of the chapter name
    dict_psychology['chapter'] = psychology.title
    #save each chapter notes
    dict_psychology['notes'] = psychology.notes

    
    return render(request,'course/psychology_notes.html',dict_psychology)

#Human-Geography
def human_geography(request):
    human_geography = Human_Geography.objects.all()
    context = {"human_geography":human_geography}

    return render(request,'course/human_geography.html',context)

def human_geogrpahy_notes(request,id):
    human_geogrpahy = Human_Geography.objects.get(id=id)
    dict_human_geogrpahy = {}

    human_geogrpahy.notes = markdown.markdown(human_geogrpahy.notes, 
    extension = [
        #包含缩进、表格等常用扩展
        'markdown.extensison.extra',
        #语法高亮扩展
        'markdown.extensions.codehilite'
    ])

    dict_human_geogrpahy['chapter'] = human_geogrpahy.title
    dict_human_geogrpahy['notes'] = human_geogrpahy.notes

    return render(request,'course/human_geogrpahy_notes.html',dict_human_geogrpahy)

    

#economics
def macroeconomics(request):
    ob = Macroeconomics.objects.all()
    context = {"Macroeconomics":ob}
    return render(request,'course/macro_econ.html',context)

def macro_notes(request,id):
    macroeconomics = Macroeconomics.objects.get(id=id)
    dict_macro_econ = {}

    macroeconomics.notes = markdown.markdown(macroeconomics.notes, 
    extension = [
        #包含缩进、表格等常用扩展
        'markdown.extensison.extra',
        #语法高亮扩展
        'markdown.extensions.codehilite'
    ])

    dict_macro_econ['chapter'] = macroeconomics.title
    dict_macro_econ['notes'] = macroeconomics.notes

    return render(request,'course/macro_econ_notes.html',dict_macro_econ)



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
def us_hisotry(request):
    ob = US_hisotry.objects.all()
    context = {"psychology":ob}
    return render(request,'course/us_history.html')