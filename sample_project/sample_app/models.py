from django.db import models
import random
# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30,default="Aditya")
    age = models.IntegerField()