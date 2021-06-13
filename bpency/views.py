from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.template import Context, loader
from django.shortcuts import render
from .models import SD, userD, BPMN

def index(request):
    return render(request, 'bpency/index.html')

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
        sd = []

        seq = sequ.split('\n')

        for i in range (len(seq)):
            x += [seq[i].replace('\r','')] 

        for i in range (len(x)):
            if ' -> ' in x[i]:
                sd += [x[i]]
            if 'opt ' in x[i]:
                sd += [x[i]]
            if 'alt ' in x[i]:
                sd += [x[i]]
            if 'ref ' in x[i]:
                sd += [x[i]]
            if x[i] == 'end alt':
                sd += [x[i]]
            if x[i] == 'end opt':
                sd += [x[i]]
            if x[i] == 'else':
                sd += [x[i]]

        task = []

        for i in range (len(sd)):

            if ' -> ' in sd[i]:
                splitt = sd[i].split(' -> ')
                task += [splitt[1]]
            if 'ref ' in sd[i]:
                splitt = sd[i].split(',')
                task += [splitt[1]]
            if sd[i] == 'end opt':
                task += ['']
                for j in range (len(sd)):
                    if 'opt ' in sd[j]:
                        splitt = sd[j-1].split(' -> ')
                        task += [splitt[1]]
            if sd[i] == 'else':
                for j in range (len(sd)):
                    if sd[j] == 'end alt':
                        if j < (len(sd)-1):
                            splitt = sd[j+1].split(' -> ')
                            task += [splitt[1]]
                task+= ['']
                for j in range (len(sd)):
                    if 'alt ' in sd[j]:
                        splitt = sd[j - 1].split(' -> ')
                        task += [splitt[1]]

        hasil = ""

        for i in range (len(task)):
            task[i] = task[i].replace('_',' ').replace('()','').replace('(',' ').replace(')',' ')
            hasil += task[i]
            hasil += "\n"

        bpmn = BPMN(code=hasil)
        bpmn.save()

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
    bpmn = BPMN.objects.all()
    return render(request, 'bpency/jajal.html')