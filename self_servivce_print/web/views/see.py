from django.shortcuts import render
from web.models import Project
from web.is_log_in import is_log_in


@is_log_in
def see(request):
    nid = request.GET.get("nid")
    proj = Project.objects.filter(id=nid)[0]
    return render(request, "web/see.html", {'proj': proj})
