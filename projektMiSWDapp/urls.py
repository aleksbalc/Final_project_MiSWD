from django.urls import path
from . import views

urlpatterns = [
    path('', views.BASE, name='BASE'),
    path('cw/', views.cw, name="cw"),
    path('lab/', views.lab, name="lab"),
    path('adddatacw/', views.adddatacw, name="adddatacw"),

    path('assignment_algorithm/', views.assignment_algorithm, name="assignment_algorithm"),
    path('assignment/', views.assignment, name="assignment"),
    path('solve_assignment/', views.solve_assignment, name='solve_assignment'),
    path('assignmentresults/<str:results>/', views.assignmentresults, name='assignmentresults'),
    path('assignment_hungarian/', views.assignment_hungarian, name="assignment_hungarian"),
    path('solve_assignment_hun/', views.solve_assignment_hun, name='solve_assignment_hun'),
    path('assignment_brute/', views.assignment_brute, name="assignment_brute"),
    path('solve_assignment_brute/', views.solve_assignment_brute, name='solve_assignment_brute'),
    path('assignment_singular_result/<str:results>/', views.assignment_singular_result, name='assignment_singular_result'),

    path('knapsack_algorithm', views.knapsack_algorithm, name='knapsack_algorithm'),
    path('knapsack/', views.knapsack, name='knapsack'),
    path('solve_knapsack/', views.solve_knapsack, name='solve_knapsack'),
    path('knapsackresults/<str:results>/', views.knapsackresults, name='knapsackresults'),
    path('knapsack_dynamic/', views.knapsack_dynamic, name="knapsack_dynamic"),
    path('solve_knapsack_dynamic/', views.solve_knapsack_dynamic, name='solve_knapsack_dynamic'),
    path('knapsack_bnb/', views.knapsack_bnb, name="knapsack_bnb"),
    path('solve_knapsack_bnb/', views.solve_knapsack_bnb, name='solve_knapsack_bnb'),
    path('knapsack_brute/', views.knapsack_brute, name="knapsack_brute"),
    path('solve_knapsack_brute/', views.solve_knapsack_brute, name='solve_knapsack_brute'),
    path('knapsack_singular_result/<str:results>/', views.knapsack_singular_result, name='knapsack_singular_result'),


    
]
