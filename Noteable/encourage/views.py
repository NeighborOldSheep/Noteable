from django.shortcuts import render

# Create your views here.

#encourage page
def index(request):
    return render(request,"encourage/index.html")