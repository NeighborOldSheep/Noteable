from django.urls import path 
from . import views
#from .views import PsychologyNotes


urlpatterns = [
    path("",views.course, name="course"),
    path("psychology/", views.psychology, name='psychology'), #psychology page
    path('psychology/<int:id>',views.psychology_notes, name="psychology_notes"),#psychology notes
    path("human-geography/", views.human_geography, name='human_geography'), #human_geography page
    path("human-geography/<int:id>", views.human_geogrpahy_notes, name='human_geography_notes'), #human_geography page
    path("economics/", views.economics, name='economics'), #economics page
    path("env_science/", views.env_science, name='env_science'), #env_sciencey page
    path("world_hisotry/", views.world_history, name='world_history'), #psychology page
    path("seminar/", views.seminar, name='seminar'), #psychology page 

]