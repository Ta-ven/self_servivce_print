from django.shortcuts import render,redirect


def is_log_in(fun):
    def inner(request, *args, **kwargs):
        if request.session.get("is_login"):
            return fun(request, *args, **kwargs)
        else:
            return redirect('/login.html')
    return inner

