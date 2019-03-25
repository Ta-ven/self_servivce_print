from django.shortcuts import render,HttpResponse
from web.models import Project, Time, Content
from web import form
import datetime
import json


def add(request):
    if request.method == "GET":
        obj = form.Add_Form()
        return render(request, 'web/add.html', {"obj": obj})
    elif request.method == "POST":
        ret = {"status": False, "msg": None}
        obj = form.Add_Form(request.POST)
        if obj.is_valid():
            ret['status'] = True
            pro_name = request.POST.get('pro_name')
            team_leader = request.POST.get('team_leader')
            summary = request.POST.get('summary')
            content = request.POST.get('content')
            comments = request.POST.get('comments')
            T = datetime.datetime.now()
            p = Project.objects.create(pro_name=pro_name, team_leader=team_leader, summary=summary, status=1)
            Content.objects.create(content=content, comments=comments, PC_id=p.id)
            Time.objects.create(add_time=T, PT_id=p.id)
        else:
            print('===========================')
            ret['msg'] = obj.errors
        return HttpResponse(json.dumps(ret))
