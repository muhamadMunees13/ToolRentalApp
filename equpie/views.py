from django.shortcuts import render
from django.http import HttpResponse
from .models import login
from .models import products
from .models import prent
from .models import lrent
import datetime

def index(request):
    return render(request,'index.html')
def home(request):
    return render(request,'home.html')
def create(request):
    return render(request,'create.html')
def success(request):
    name = request.POST['name']
    password = request.POST['pwd']
    proof = request.POST['proof']
    idimg = request.FILES['idimg']
    pnum = request.POST['pnum']
    data = login (name=name,password=password,proof=proof,idimg=idimg,pnum=pnum)
    data.save()
    return render(request,'success.html')
def log(request):
    name = request.POST['user']
    password = request.POST['password']
    login.objects.filter(name=name, password=password)
    data=products.objects.all()
    if name=='company' and password=='6543':
        return render(request, 'company.html')
    elif login.objects.filter(name=name, password=password):
        request.session['name'] = name
        return render(request, 'user.html',{'data':data})
    else:
        return render(request,'logerror.html')
def user(requset):
    return render(requset,'user.html')
def logerror(request):
    return render(request,'logerror.html')
def company(requset):
    return render(requset,'company.html')
def cadd(request):
    return render(request,'cadd.html')
def logins(request):
    return render(request,'logins.html')
def logi(request):
    data=login.objects.all()
    return render(request,'logi.html',{'data':data})
def edit(request):
    return render(request,'edit.html')
def uedits(request):
    data = products.objects.all()
    return render(request,'uedits.html',{'data':data})
def edited(request):
    pname = request.session['prod']
    pprice=request.POST['p_price']
    data=products.objects.get(pname=pname)
    data.rent=pprice
    data.save()
    return render(request,'edited.html')
def save(request):
    pname = request.POST['pname']
    rent = request.POST['rent']
    detail = request.POST['detail']
    image = request.FILES['image']
    data = products(pname=pname,rent=rent, detail=detail, image=image)
    data.save()
    return render(request, 'save.html')
def bill(request):
    name=request.session['name']
    data= login.objects.filter(name=name)
    prod = request.POST['pname']
    request.session['prod'] = prod
    rents = request.POST['rent']
    request.session['rents'] = rents
    b=lrent(prod=prod, rentl=rents)
    b.save()
    return render(request,'bill.html',{'data':data})
def take(request):
    try:
        retn= request.POST['retn']
        ndays = request.POST['ndays']
        username = request.session['name']
        time = datetime.datetime.now()

        rrent = request.session['rents']
        torent = int(ndays)*int(rrent)
        product = request.session['prod']

        data = prent(username=username, time=time,orent=rrent,retn=retn,ndays=ndays,product=product,torent=torent)
        data.save()
        data=prent.objects.all()
        return render(request,'take.html',{'data':data})
    except:
        return render(request,'rerror.html')
def rerror(request):
    return render(request, 'rerror.html')

def logout(request):
    try:
        del request.session['name']
    except:
        return render(request,'home.html')
    return render(request,'home.html')
def rentals(request):
    data = prent.objects.all()
    return render(request, 'rentals.html', {'data': data})
def userid(request):
    name = request.session['name']
    data = prent.objects.filter(username=name)
    return render(request,'userid.html',{'data':data})
def contact(request):
    return render(request, 'contact.html')
def about(request):
    return render(request, 'about.html')
