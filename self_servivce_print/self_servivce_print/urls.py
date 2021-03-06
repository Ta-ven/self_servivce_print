from django.contrib import admin
from django.urls import path, include
from web.views import home
from web.views import find
from web.views import add
from web.views import see
from web.views import delete
from web.views import modify

urlpatterns = [
    path('home.html/', home.home, name='home.html/'),
    path('admin/', admin.site.urls),
    path('allproject.html/', find.allproject, name='allproject.html/'),
    path('finish.html/', find.finish, name='finish.html/'),
    path('initial.html/', find.initial, name='initial.html/'),
    path('medium.html/', find.medium, name='medium.html/'),
    path('last.html/', find.last, name='last.html/'),
    path('search.html/', find.search, name='search.html/'),
    path('add.html/', add.add, name='add.html/'),
    path('see.html/', see.see, name='see.html/'),
    path('del.html/', delete.delete, name='del.html/'),
    path('modify.html/', modify.modify, name='modify.html/'),

    path('', include('status.urls')),
]
