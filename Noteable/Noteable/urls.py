"""Noteable URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("Home.urls")),  #默认网址访问的网页
    path('course/',include("course.urls")), #访问Ap Course页面路由
    path('encourage/',include('encourage.urls')),#访问encourage页面路由
    path('exam/',include('exam.urls')),#访问做题页面路由
    path('aboutus/',include('aboutus.urls')) #访问about us页面路由
]
