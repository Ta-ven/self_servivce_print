from django.shortcuts import HttpResponse
import json
from web.models import Project
from web.is_log_in import is_log_in


@is_log_in
def delete(requset):
    status = {'status': 0, 'msg': None}
    try:
        action = int(requset.POST.get("action"))
        nid = int(requset.POST.get("nid"))
        if action == 1:
            status['status'] = 1
            Project.objects.filter(id=nid).delete()
        return HttpResponse(json.dumps(status))
    except Exception:
        status['msg'] = '删除错误！'
        return HttpResponse(json.dumps(status))
