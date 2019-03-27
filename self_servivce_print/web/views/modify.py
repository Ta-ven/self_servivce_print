from django.shortcuts import render, HttpResponse
from web.models import Project, Content
import json
from web.is_log_in import is_log_in



@is_log_in
def modify(request):

    if request.method == "GET":
        nid = request.GET.get("nid")
        proj = Project.objects.filter(id=nid)[0]
        return render(request, "modify/modify.html", {'proj': proj})
    else:
        sta = {"status": 0, 'msg': None}
        try:
            sta['status'] = 1
            nid = int(request.POST.get('nid'))
            status = int(request.POST.get('status'))
            pro_name = request.POST.get('pro_name')
            team_leader = request.POST.get('team_leader')
            summary = request.POST.get('summary')
            content = request.POST.get('content')
            comments = request.POST.get('comments')
            Project.objects.filter(id=nid).update(pro_name=pro_name,
                                                  team_leader=team_leader,
                                                  status=status,
                                                  summary=summary
                                                  )
            Content.objects.filter(PC_id=nid).update(content=content,
                                                     comments=comments)
            return HttpResponse(json.dumps(sta))
        except Exception:
            sta["msg"] = "修改错误"
            return HttpResponse(json.dumps(sta))
