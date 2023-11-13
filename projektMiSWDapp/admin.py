from django.contrib import admin
from .models import TestModel, DataSets, KnapsackData, AssignmentData

# Register your models here.

admin.site.register(TestModel)
admin.site.register(DataSets)
admin.site.register(KnapsackData)
admin.site.register(AssignmentData)