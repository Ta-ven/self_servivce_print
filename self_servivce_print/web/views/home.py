from django.shortcuts import render
from web.is_log_in import is_log_in



@is_log_in
def home(request):

    return render(request, 'base/base.html')