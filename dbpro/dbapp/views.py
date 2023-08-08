from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def home(request):
    return render(request, 'form.html')
def savedata(request):
    b=Book()
    b.bname=request.GET.get('bname')
    b.bauthor=request.GET.get('bauthor')
    b.bdesc=request.GET.get('bdesc')
    b.bprice=request.GET.get('bprice')
    b.save()
    return HttpResponse("<h1> Data saved</h1>")
def getdata(request):
    data =Book.objects.all()
    # dict={'bname':'javas','bauthor':'mrbean'}
    return render(request,'display.html',{'data':data})