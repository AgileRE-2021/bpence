import hashlib

from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.template import Context, loader
from django.shortcuts import render, redirect
from .models import SD, userD, BPMN
from django.contrib import messages

def index(request):
    return render(request, 'bpency/index.html')

def indexacc(request):
    return render(request, 'bpency/index-logged.html')

def login_view(request):
    return render(request, 'bpency/login.html')

def signup_view(request):
    return render(request, 'bpency/signup.html')

def konversi(request):
    if request.method == 'POST':
        sequ = request.POST["codeplant"]
        sd = SD(code=sequ)
        sd.save()

        x = []
        sd1 = []

        seq = sequ.split('\n')

        for i in range (len(seq)):
            x += [seq[i].replace('\r','')] 

        if '@startuml' in x[0]:
            if '@enduml' in x[-1]:
                for i in range (len(x)):
                    if ' -> ' in x[i]:
                        sd1 += [x[i]]
                    if 'opt ' in x[i]:
                        sd1 += [x[i]]
                    if 'alt ' in x[i]:
                        sd1 += [x[i]]
                    if 'ref ' in x[i]:
                        sd1 += [x[i]]
                    if x[i] == 'end alt':
                        sd1 += [x[i]]
                    if x[i] == 'end opt':
                        sd1 += [x[i]]
                    if x[i] == 'else':
                        sd1 += [x[i]]

                task = []

                for i in range (len(sd1)):

                    if ' -> ' in sd1[i]:
                        splitt = sd1[i].split(' -> ')
                        task += [splitt[1]]
                    if 'ref ' in sd1[i]:
                        splitt = sd1[i].split(',')
                        task += [splitt[1]]
                    if sd1[i] == 'end opt':
                        task += ['']
                        for j in range (len(sd1)):
                            if 'opt ' in sd1[j]:
                                splitt = sd1[j-1].split(' -> ')
                                task += [splitt[1]]
                    if sd1[i] == 'else':
                        for j in range (len(sd1)):
                            if sd1[j] == 'end alt':
                                if j < (len(sd1)-1):
                                    splitt = sd1[j+1].split(' -> ')
                                    task += [splitt[1]]
                        task+= ['']
                        for j in range (len(sd1)):
                            if 'alt ' in sd1[j]:
                                splitt = sd1[j - 1].split(' -> ')
                                task += [splitt[1]]

                hasil = ""

                for i in range (len(task)):
                    task[i] = task[i].replace('_',' ').replace('()','').replace('(',' ').replace(')',' ').replace('"','')
                    hasil += task[i]
                    hasil += "\n"

                bpmn = BPMN(code=hasil)
                sd.save()
                bpmn.save()
                return HttpResponseRedirect("/hasil")
            else:
                messages.error(request, "there is no @enduml!")
        else:
            messages.error(request, "there is no @startuml")

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

def hasil(request):
    bpmns = BPMN.objects.last()
    context = {
        'bpmns':bpmns,
    }
    return render(request, 'bpency/hasil.html',context)

def konvload(request):
    return render(request, 'bpency/konv-load.html')

def histori(request):
    SDs = SD.objects.all()
    return render(request, 'bpency/histori.html', {'SDs': SDs})

def edit (request, id):
    SDs = SD.objects.get(id=id)
    return render(request, 'bpency/edit.html', {'SDs':SDs})

def update(request, id):
    SDs = SD.objects.get(id=id)

    if request.method == 'POST':
        sds = request.POST["codeplant"]
        sd = SD.objects.filter(id=id)
        for s in sd :
            s.code=sds
            s.save()
        return redirect("/hasil")

    return render(request, 'bpency/edit.html', {'SDs':SDs})
def destroy(request, id):
    SDs = SD.objects.get(id=id)
    SDs.delete()
    return redirect("/history")

