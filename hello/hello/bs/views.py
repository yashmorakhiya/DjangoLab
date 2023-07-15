from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return render(request,"index.html")

# Create your views here.
def about(request):
    return render(request,"other/about.html")
def services(request):
    return render(request,"other/services.html")
def contact(request):
    return render(request,"other/contact.html")
def blog(request):
    return render(request,"other/blog.html")