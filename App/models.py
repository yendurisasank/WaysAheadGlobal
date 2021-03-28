from django.db import models

# Create your models here.
class DataM(models.Model):
    education = models.CharField(max_length=200) 
    marital_education =	models.CharField(max_length=200) 
    default	=models.CharField(max_length=200) 
    job	=models.CharField(max_length=200) 
    targeted =models.CharField(max_length=200) 
    marital	=models.CharField(max_length=200) 
    housing	=models.CharField(max_length=200) 
    month =models.CharField(max_length=200) 
    loan = models.CharField(max_length=200) 