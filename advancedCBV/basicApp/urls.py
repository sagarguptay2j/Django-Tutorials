from django.urls import path
from basicApp import views

app_name = 'basicApp'
urlpatterns = [
    path('',views.SchoolListVIew.as_view(),name = 'list'),
    path('<int:pk>',views.SchoolDetailView.as_view(),name = 'detail'),
    path('create/',views.SchoolCreateView.as_view(),name = 'create'),
    path('update/<int:pk>/',views.SchoolUpdateView.as_view(),name = 'update'),
    path('delete/<int:pk>/',views.SchoolDeleteView.as_view(),name = 'delete'),
]
