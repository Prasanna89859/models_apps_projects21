from django.db import models

# Create your models here.
from app1.views import *

class topics(models.Model):
    topics_name=models.CharField(max_length=100,primary_key=True)
    url=models.IntegerField()

class webpage(models.Model):
    tname=models.ForeignKey(topics,on_delete=models.CASCADE)
    ename=models.CharField(max_length=100)
    Email=models.EmailField()
    
    
    
