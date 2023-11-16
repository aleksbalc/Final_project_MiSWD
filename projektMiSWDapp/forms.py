import re
from django import forms
from django.forms import ModelForm
from .models import KnapsackData, AssignmentData


class KnapsackDataForm(ModelForm):
    class Meta:
        model = KnapsackData
        fields = ['name', 'val', 'wt', 'W']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Nazwa zestawu danych'
        self.fields['val'].widget.attrs['placeholder'] = 'Wartości przemiotów'
        self.fields['wt'].widget.attrs['placeholder'] = 'Wagi przedmiotów'
        self.fields['W'].widget.attrs['placeholder'] = 'Maksymalna waga plecaka'

    def validate(self):
        val = self.cleaned_data['val']
        wt = self.cleaned_data['wt']
        regex = r'^[0-9 ]+$'
        if not re.match(regex, val) or not re.match(regex, wt):
            return False
        W = self.cleaned_data['W']
        regex = r'^\d+$'
        if not re.match(regex, W) or int(W) <= 0:
            return False
        return True

class AssignmentDataForm(ModelForm):
    class Meta:
        model = AssignmentData
        fields = ['name', 'matrix']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Nazwa zestawu danych'
        self.fields['matrix'].widget.attrs['placeholder'] = 'Macierz przyporządkowań'

    def validate(self):
        matrix = self.cleaned_data['matrix']
        regex = r'^[0-9 \n]+$'
        if not re.match(regex, matrix):
            return False
        return True

class KnapsackForm(forms.Form):
   datasets = forms.ModelMultipleChoiceField(queryset=KnapsackData.objects.all())