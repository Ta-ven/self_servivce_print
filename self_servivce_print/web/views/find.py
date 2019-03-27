from django.shortcuts import render
from django.db.models import Q
from web.models import Project, Time
from statics.pagination import Pagination
from web.is_log_in import is_log_in

@is_log_in
def home(request):
    return render(request, 'base/base.html')

def searchs(fun,page,request):
    start = (page-1)*10
    end = page*10
    status = {'allproject': 5, 'finish': 4, 'last': 3, 'medium': 2, 'initial': 1}
    searches = request.GET.get('search')
    if searches is None and status[fun.__name__] != 5:
        count = Project.objects.filter(status=status[fun.__name__]).count()
        projects = Project.objects.filter(status=status[fun.__name__])
    elif searches is None and status[fun.__name__] == 5:
        count = Project.objects.all().count()
        projects = Project.objects.all()[start:end]
    else:
        if status[fun.__name__] == 5:
            try:
                searches = int(searches)
                projects = Project.objects.filter(id=searches)
                count = 1
            except Exception:
                count = Project.objects.filter(Q(pro_name__icontains=searches) |
                                                  Q(team_leader__icontains=searches)).count()
                projects = Project.objects.filter(Q(pro_name__icontains=searches) |
                                                  Q(team_leader__icontains=searches))[start:end]
        else:
            try:
                searches = int(searches)
                projects = Project.objects.filter(status=status[fun.__name__], id=searches)
                count = 1
            except Exception:
                count = Project.objects.filter(Q(status=status[fun.__name__]) &
                                               (Q(pro_name__icontains=searches) |
                                                Q(team_leader__icontains=searches))).count()
                projects = Project.objects.filter(Q(status=status[fun.__name__]) &
                                               (Q(pro_name__icontains=searches) |
                                                Q(team_leader__icontains=searches)))[start:end]
    return count, projects

# 装饰器   查询

def search(fun):
    def inner(request, *args, **kwargs):
        page = request.GET.get('Page')
        try:
            page = int(page)
        except Exception:
            page = 1
        count, projects = searchs(fun, page, request)
        return fun(request, projects, count, page, *args, **kwargs)
    return inner


@is_log_in
@search
def allproject(request, projects, count, page):
    print(request.session.get('uuid'))
    obj = Pagination(count, page, "allproject.html")
    return render(request, 'web/all_projects.html', {'projects': projects, "count": count, 'obj': obj})

@is_log_in
@search
def finish(request, projects, count, page):
    obj = Pagination(count, page, "finish.html")
    return render(request, 'web/finish.html', {'projects': projects, "count": count, 'obj': obj})


@is_log_in
@search
def initial(request, projects, count, page):
    obj = Pagination(count, page, "initial.html")
    return render(request, 'web/initial.html', {'projects': projects, "count": count, 'obj': obj})

@is_log_in
@search
def medium(request, projects, count, page):
    obj = Pagination(count, page, "medium.html")
    return render(request, 'web/medium.html', {'projects': projects, "count": count, 'obj': obj})

@is_log_in
@search
def last(request, projects,  count, page):
    obj = Pagination(count, page, "last.html")
    return render(request, 'web/last.html', {'projects': projects, "count": count, 'obj': obj})
