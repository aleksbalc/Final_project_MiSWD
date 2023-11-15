from django.shortcuts import render, redirect
from .models import KnapsackData, AssignmentData
from django.http import HttpResponseRedirect
from .forms import KnapsackDataForm, AssignmentDataForm

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