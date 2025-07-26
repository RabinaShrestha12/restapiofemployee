from django.db import models

# Create your models here.
class Employee(models.Model):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    salary = models.CharField(max_length=200)
    age = models.CharField(max_length=200)