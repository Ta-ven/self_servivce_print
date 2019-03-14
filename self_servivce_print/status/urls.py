from django.urls import path, include
from status import views

urlpatterns = [
    path('login.html/', views.login, name='login.html/'),
]