from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render
from .models import SD

def index(request):
    return render(request, 'bpency/index.html')

def login_view(request):
    return render(request, 'bpency/login.html')

def signup_view(request):
    return render(request, 'bpency/signup.html')

def konversi(request):
    if request.method == 'POST':
        sd = SD(code=request.POST["codeplant"])
        sd.save()

    return render(request, 'bpency/konversi.html')