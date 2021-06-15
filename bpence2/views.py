from django.shortcuts import render

def konvload(request):
    return render(request, 'konv-load.html')

def konvresult(request):
    return render(request, 'konv-result.html')

def signupconf(request):
    return render(request, 'signup-conf.html')