from django.shortcuts import render
from django.http import HttpResponse
from formApp  import forms

# Create your views here.
def index(request):
    return render(request,'formApp/index.html')

def formPage(request):
    form = forms.formName()

    if request.method == 'POST':
        form = forms.formName(request.POST)

        if form.is_valid():
            print("Validation SUccessful")
            print("Name: "+form.cleaned_data['name'])
            print("Email: "+form.cleaned_data['email'])
            print("Text: "+form.cleaned_data['text'])
    return render(request,'formApp/formPage.html',{'form':form})
