from django.db import models

class Student_Info(models.Model):
    ID = models.CharField(max_length=8)
    NAME = models.CharField(max_length=50)
    CLASS = models.CharField(max_length=10)
    FACULTY = models.CharField(max_length=30)
    AGE = models.IntegerField()
