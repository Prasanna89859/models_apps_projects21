from django.db import models


# Create your models here.

from app2.models import *

class country(models.Model):
    Cname=models.CharField(max_length=100,primary_key=True)
    Ccode=models.IntegerField()

class capital(models.Model):
    cname=models.OneToOneField(country,on_delete=models.CASCADE)
    ccapital=models.IntegerField()
