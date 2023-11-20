import json
import numpy as np

from django.shortcuts import render, redirect
from .models import KnapsackData, AssignmentData
from django.http import HttpResponseRedirect
from .forms import KnapsackDataForm, AssignmentDataForm, KnapsackForm
from .solvingalgorithms import *

class NpEncoder(json.JSONEncoder):
   def default(self, obj):
       if isinstance(obj, np.int32):
           return int(obj)
       return json.JSONEncoder.default(self, obj)

def BASE(request):
    return render(request, 'index.html', {} )

def cw(request):
    return render(request, 'cw.html')

def lab(request):
    return render(request, 'lab.html')

def adddatacw(request):
    ksubmitted = False
    asubmitted = False
    if request.method == "POST":
        knapsackForm = KnapsackDataForm(request.POST)
        assignmentForm = AssignmentDataForm(request.POST)

        if knapsackForm.is_valid():
            knapsackForm.save()
            if asubmitted == False:
                return HttpResponseRedirect('/adddatacw?ksubmitted=True')
            else:
                return HttpResponseRedirect('/adddatacw?ksubmitted=True&asubmitted=True')

        
        if assignmentForm.is_valid():
            assignmentForm.save()
            if ksubmitted == False:
                return HttpResponseRedirect('/adddatacw?asubmitted=True')
            else:
                return HttpResponseRedirect('/adddatacw?ksubmitted=True&asubmitted=True')
    else:
        knapsackForm = KnapsackDataForm()
        assignmentForm = AssignmentDataForm()

        if 'ksubmitted' in request.GET:
            ksubmitted = True
            return render(request, 'adddatacw.html', {'knapsackForm':knapsackForm, 'assignmentForm':assignmentForm, 'ksubmitted':ksubmitted, 'asubmitted':asubmitted})
        
        if 'asubmitted' in request.GET:
            asubmitted = True
            return render(request, 'adddatacw.html', {'knapsackForm':knapsackForm, 'assignmentForm':assignmentForm, 'ksubmitted':ksubmitted, 'asubmitted':asubmitted})


    return render(request, 'adddatacw.html', {'knapsackForm':knapsackForm, 'assignmentForm':assignmentForm})

def knapsack(request):
    datasets = KnapsackData.objects.all()
    return render(request, 'knapsack.html', {'datasets': datasets})

def solve_knapsack(request):
 if request.method == 'POST':
     selected_dataset_ids = request.POST.getlist('datasets')
     selected_datasets = KnapsackData.objects.filter(pk__in=selected_dataset_ids)

     # Perform knapsack calculations
     results = []
     for dataset in selected_datasets:
         W = dataset.W
         wt = [int(w) for w in dataset.wt.split(' ')] # Convert wt string to list of integers
         val = [int(v) for v in dataset.val.split(' ')] # Convert val string to list of integers

         n = min(len(wt), len(val))
         # Perform knapsack algorithm here and store the result in the results list
         # For example, let's assume a simple calculation for demonstration purposes:
         result_dyn = knapsackDynamic(val, wt, W)
         print("calculated dynamic")
         result_bnb = knapsackBnB_sorted(val, wt, W)
         print("calculated bnb")
         result_bru = knapsack_brute_force(val, wt, W)
         print("calculated brute")
         results.append((dataset.name, int(W), wt, val, list(range(n)), result_bru, result_bnb, result_dyn)) # Append a tuple of dataset name and result

     # Serialize the results list and redirect to the results page with the calculated data
     return redirect('knapsackresults', results = json.dumps(results))
 return redirect('knapsack')

def knapsackresults(request, results):
 results = json.loads(results)
 return render(request, 'knapsackresults.html', {'results': results})



def assignment(request):
    datasets = AssignmentData.objects.all()
    return render(request, 'assignment.html', {'datasets': datasets})

def solve_assignment(request):
 if request.method == 'POST':
    selected_dataset_ids = request.POST.getlist('datasets')
    selected_datasets = AssignmentData.objects.filter(pk__in=selected_dataset_ids)

    results = []
    for dataset in selected_datasets:
        # Fetch the data from your model
        dataset = AssignmentData.objects.get(name=dataset.name)

        # Convert the matrix string into a list of integers
        matrix_data = [int(i) for i in dataset.matrix.split()]

        # Reshape the list into a matrix
        matrix = np.array(matrix_data).reshape(dataset.n, dataset.n)
        matrix_list = matrix.tolist()
        # Perform assignment algorithm here and store the result in the results list
        # For example, let's assume a simple calculation for demonstration purposes:
        result_hun = hungarian_algorithm(matrix)
        results.append((dataset.name, matrix_list, dataset.n, result_hun)) # Append a tuple of dataset name and result


     # Serialize the results list and redirect to the results page with the calculated data
    return redirect('assignmentresults', results = json.dumps(results))
 return redirect('assignment')

def assignmentresults(request, results):
 results = json.loads(results)
 return render(request, 'assignmentresults.html', {'results': results})
