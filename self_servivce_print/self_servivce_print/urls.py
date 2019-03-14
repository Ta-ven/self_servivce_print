"""self_servivce_print URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from web import views

urlpatterns = [
    path('home.html/', views.home, name='home.html/'),
    path('admin/', admin.site.urls),
    path('allproject.html/', views.allproject, name='allproject.html/'),
    path('finish.html/', views.finish, name='finish.html/'),
    path('initial.html/', views.initial, name='initial.html/'),
    path('medium.html/', views.medium, name='medium.html/'),
    path('last.html/', views.last, name='last.html/'),
    path('', include('status.urls')),
]
