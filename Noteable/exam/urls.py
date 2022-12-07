from django.urls import path
from exam.views import *

urlpatterns = [
    path('',IndexView.as_view(), name='exam') #刷题页面首页
]