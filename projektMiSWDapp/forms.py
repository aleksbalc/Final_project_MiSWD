from django import forms
from .models import DataSets, KnapsackData, AssignmentData

class DataSetsForm(forms.ModelForm):
    class Meta:
        model = DataSets
        fields = ['name', 'dataType']

class KnapsackDataForm(forms.ModelForm):
    class Meta:
        model = KnapsackData
        fields = ['dataset', 'val', 'wt', 'W']

class AssignmentDataForm(forms.ModelForm):
    class Meta:
        model = AssignmentData
        fields = ['dataset', 'matrix']