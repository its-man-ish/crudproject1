from django.db import models

# Create your models here.

class StudentModel(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    grade = models.IntegerField()
