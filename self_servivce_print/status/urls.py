from django.urls import path, include
from status import views

urlpatterns = [
    path('login.html/', views.login, name='login.html/'),
    path('logout.html/', views.logout, name='logout.html/'),
    path('register.html/', views.register, name='register.html/'),
]