from django.shortcuts import render
from django.http import HttpResponse
from testApp.forms import formName
# Create your views here.

def index(request):
    return render(request,'testApp/index.html')


def users(request):
    form = formName()

    if request.method == 'POST':
        form = formName(request.POST)
        if form.is_valid():
            form.save(commit = True)
            return index(request)
        else:
            print("Invalid form")
    return render(request,"testApp/user.html",{'form':form})
