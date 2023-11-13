from django.urls import path
from . import views

urlpatterns = [
    path('', views.BASE, name='BASE'),
    path('testsets/', views.testset, name="testset"),
    path('cw/', views.cw, name="cw"),
    path('lab/', views.lab, name="lab")
]
