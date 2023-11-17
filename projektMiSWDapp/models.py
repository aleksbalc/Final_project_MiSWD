from django.db import models

# KnapsackData model
class KnapsackData(models.Model):
    name = models.CharField(max_length=100)
    val = models.CharField(max_length=255)  # Consider adjusting the max_length according to your data
    wt = models.CharField(max_length=255)  # Adjust max_length based on your data
    W = models.IntegerField()

# AssignmentData model
class AssignmentData(models.Model):
    name = models.CharField(max_length=100)
    matrix = models.TextField()  # Use TextField for longer sequences of data
    n = models.IntegerField()
    