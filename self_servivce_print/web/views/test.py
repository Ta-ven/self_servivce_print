from django.shortcuts import render,HttpResponse


def test(request):
    print(request.GET)
    return render(request, 'test.html')