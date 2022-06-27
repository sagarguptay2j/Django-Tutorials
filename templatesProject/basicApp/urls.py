from django.urls import path
from . import views

app_name = 'basicApp'

urlpatterns = [
    path('index/',views.index,name = 'index'),
    path('other/',views.other,name = 'other'),
]
