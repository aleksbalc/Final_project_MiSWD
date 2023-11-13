from django.db import models

# Create your models here.
class TestModel(models.Model):
    name = models.CharField(max_length=200)

    
# DataSets model
class DataSets(models.Model):
    name = models.CharField(max_length=100)
    DATA_TYPES = (
        ('knapsack', 'Knapsack'),
        ('assignment', 'Assignment'),
        ('optimization', 'Optimization'),
    )
    dataType = models.CharField(max_length=20, choices=DATA_TYPES)

# KnapsackData model
class KnapsackData(models.Model):
    dataset = models.OneToOneField(DataSets, on_delete=models.CASCADE, limit_choices_to={'dataType': 'knapsack'})
    val = models.CharField(max_length=255)  # Consider adjusting the max_length according to your data
    wt = models.CharField(max_length=255)  # Adjust max_length based on your data
    W = models.IntegerField()

# AssignmentData model
class AssignmentData(models.Model):
    dataset = models.OneToOneField(DataSets, on_delete=models.CASCADE, limit_choices_to={'dataType': 'assignment'})
    matrix = models.TextField()  # Use TextField for longer sequences of data