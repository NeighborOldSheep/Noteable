from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='exam'), #刷题页面首页
    path('psychology_test/', views.psycology_test, name='psychology_test'), #psychology test
    path('world_history_test',views.world_history_test ,name='world_history_test'), #world_history test
    path('macro_economic_test',views.macro_economic_test,name="macro_economic_test"), #macro econ test
    path('physics_A_test',views.physics_A_test,name='physics_A_test'), # physics A test
]