from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render

def index(request):
    return render(request, 'bpency/index.html')

def nav(request):
    return render(request, 'bpency/nav.html')

def konversi(request):
    return render(request, 'bpency/konversi.html')