from django.db import models
from datetime import datetime

from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=500)
    postalCode = models.IntegerField()

class Faculty(models.Model):
    name = CharField(max_length=50)

class CertificateType(models.Model):
    name = models.CharField(max_length=50)

class Department(models.Model):
    name = models.CharField(max_length=50)
    Faculty = models.ForeignKey(Faculty, on_delete = models.CASCADE)

class Grade(models.Model):
    name = models.IntegerField()

class Student(models.Model):
    fullName = models.CharField(max_length=400)
    yearOfGraduation = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=CASCADE)
    school = models.ForeignKey(School, on_delete=CASCADE)
    certificate = models.ForeignKey(CertificateType, on_delete=CASCADE)

