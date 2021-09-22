from django.db import models
from datetime import date

from django.db.models.fields import DateField
# Create your models here.

class Task(models.Model):
    Tasktytle= models.CharField(max_length=50)
    TaskDe = models.TextField()
    TaskDate = models.DateField(default=date.today())



class task2(models.Model):
    tasktitle = models.CharField(max_length=50)
    taskdes = models.TextField()
    taskdate = models.DateField(default=date.today())







