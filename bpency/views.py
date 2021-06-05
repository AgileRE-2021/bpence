from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render
from .models import SD, userD
import hashlib

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

def login(request):        
    return render(request, 'bpency/login.html')

def signup(request):
    
    if request.method == 'POST':
        nama=request.POST["name"]
        email=request.POST["email"]
        passw=request.POST["password"]
        passw = hashlib.sha256(str.encode(passw)).hexdigest()
        usr = userD(nama=nama, email=email, passw=passw)
        usr.save()
    return render(request, 'bpency/signup.html')

def jajal(request):
    return render(request, 'bpency/jajal.html')