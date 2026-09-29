from django.db import models

# Create your models here.

class Cathedra(models.Model):
    name = models.CharField()
    head = models.CharField()

class Program(models.Model):
    code = models.IntegerField()
    name = models.CharField()
    description = models.CharField()
    coordinator_name = models.CharField()
    coordinator_contact = models.CharField()
    graduation_cathedra = models.ForeignKey(Cathedra, on_delete=models.CASCADE)
    discipline_list = models.JSONField(default=list)

class Lecturer(models.Model):
    name = models.CharField()
    role = models.CharField()
    degree = models.CharField()
    cathedra = models.ForeignKey(Cathedra, on_delete=models.CASCADE)
