from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'basicApp/index.html')

def home(request):
    return render(request,'basicApp/base.html')

def other(request):
    return render(request,'basicApp/other.html')
