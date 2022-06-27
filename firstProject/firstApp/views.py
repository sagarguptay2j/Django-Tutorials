from django.shortcuts import render
from django.http import HttpResponse
from firstApp.models import AccessRecord,Webpage,Topic


# Create your views here.
def index(request):
    webPageList = AccessRecord.objects.order_by('date')
    myDir={'access_record':webPageList}
    return render(request,"firstApp/index.html",context=myDir)

def help(request):
    myDir={'help_me':'from help_me'}
    return render(request,"firstApp/help.html",context=myDir)
