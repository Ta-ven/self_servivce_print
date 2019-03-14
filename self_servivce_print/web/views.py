from django.shortcuts import render
from self_servivce_print import settings
from web.models import Project, Time

def home(request):
    return render(request, 'base/base.html')


def allproject(request):
    all_proj = Project.objects.all()
    return render(request, 'web/all_projects.html', {'all_proj': all_proj})


def finish(request):
    finish_projs = Project.objects.filter(status=4)
    return render(request, 'web/finish.html', {'finish_projs': finish_projs})


def initial(request):
    initial_projs = Project.objects.filter(status=1)
    return render(request, 'web/initial.html', {'initial_projs': initial_projs})


def medium(request):
    medium_projs = Project.objects.filter(status=2)
    return render(request, 'web/medium.html', {'medium_projs': medium_projs})


def last(request):
    last_projs = Project.objects.filter(status=3)
    return render(request, 'web/last.html', {'last_projs': last_projs})


