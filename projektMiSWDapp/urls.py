from django.urls import path
from . import views

urlpatterns = [
    path('', views.BASE, name='BASE'),
    path('cw/', views.cw, name="cw"),
    path('lab/', views.lab, name="lab"),
    path('adddatacw/', views.adddatacw, name="adddatacw")
]
