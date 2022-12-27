from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='exam'), #刷题页面首页
    path('psychology_test/', views.psycology_test, name='psychology_test'), #psychology test
    path('world_history_test',views.world_history_test ,name='world_history_test') #world_history test
]