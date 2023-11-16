from django.urls import path
from . import views

urlpatterns = [
    path('', views.BASE, name='BASE'),
    path('cw/', views.cw, name="cw"),
    path('lab/', views.lab, name="lab"),
    path('adddatacw/', views.adddatacw, name="adddatacw"),
    path('knapsack/', views.knapsack, name='knapsack'),
    path('solve_knapsack/', views.solve_knapsack, name='solve_knapsack'),
    path('knapsackresults/<str:results>/', views.knapsackresults, name='knapsackresults')

]
