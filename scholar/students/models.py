from django.db import models
class User(models.Model):
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    dni=models.CharField(max_length=10,default="")
    age=models.IntegerField(default=0)
# Create your models here.


