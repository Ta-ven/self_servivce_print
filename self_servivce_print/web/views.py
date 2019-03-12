from django.shortcuts import render
from self_servivce_print import settings


def home(request):
    return render(request, 'base/base.html')


def allproject(request):
    return render(request, 'web/all_projects.html')


def finish(request):
    return render(request, 'web/finish.html')


def initial(request):
    return render(request, 'web/initial.html')


def medium(request):
    return render(request, 'web/medium.html')


def last(request):
    return render(request, 'web/last.html')
