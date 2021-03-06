"""chouti URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.test),
    path('getcode/', views.getcode),
    path('next_page/', views.next_page),
    path('accomplish/', views.accomplish),
    path('logout/', views.logout, name='logout'),
    path('login/', views.login),
    path('check_code/', views.check_code, name='check_code'),
    path('allhot/', views.AllHot.as_view()),
    path('link/pic/upload/', views.upload),
    path('link/pic/praise/', views.praise),
]
