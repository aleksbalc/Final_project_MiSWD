import json
from django.shortcuts import render, redirect
from .models import KnapsackData, AssignmentData
from django.http import HttpResponseRedirect
from .forms import KnapsackDataForm, AssignmentDataForm, KnapsackForm

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

         # Perform knapsack algorithm here and store the result in the results list
         # For example, let's assume a simple calculation for demonstration purposes:
         result = W
         results.append((dataset.name, result)) # Append a tuple of dataset name and result

     # Serialize the results list and redirect to the results page with the calculated data
     return redirect('knapsackresults', results = json.dumps(results))
 return redirect('knapsack')

def knapsackresults(request, results):
 results = json.loads(results)
 return render(request, 'knapsackresults.html', {'results': results})