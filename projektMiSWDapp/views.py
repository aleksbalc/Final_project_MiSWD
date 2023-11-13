from django.shortcuts import render
from .models import TestModel, DataSets, KnapsackData, AssignmentData
from .forms import DataSetsForm, KnapsackDataForm, AssignmentDataForm

def BASE(request):
    return render(request, 'index.html' )

def testset(request):
    sets = TestModel.objects.all()
    return render(request, "testset.html", {"testsets": sets})

def add_data(request):
    if request.method == 'POST':
        data_form = DataSetsForm(request.POST)
        knapsack_form = KnapsackDataForm(request.POST)
        assignment_form = AssignmentDataForm(request.POST)
        
        if data_form.is_valid() and knapsack_form.is_valid() and assignment_form.is_valid():
            data_instance = data_form.save()
            knapsack_instance = knapsack_form.save(commit=False)
            knapsack_instance.dataset = data_instance
            knapsack_instance.save()
            assignment_instance = assignment_form.save(commit=False)
            assignment_instance.dataset = data_instance
            assignment_instance.save()
            # Redirect or do something after successful save

    else:
        data_form = DataSetsForm()
        knapsack_form = KnapsackDataForm()
        assignment_form = AssignmentDataForm()

    return render(request, 'your_template.html', {
        'data_form': data_form,
        'knapsack_form': knapsack_form,
        'assignment_form': assignment_form,
    })

def cw(request):
    return render(request, 'cw.html')

def lab(request):
    return render(request, 'lab.html')