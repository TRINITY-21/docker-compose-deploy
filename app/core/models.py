from django.db import models

# Create your models here.


class Sample(models.Model):
  attachment = models.FileField()
  name = models.CharField(max_length=100)
  age = models.IntegerField(default=10)
  lastname = models.CharField(max_length=100)
  firstname = models.CharField(max_length=100)



class SampleTwo(models.Model):
  attachment = models.FileField()
  name = models.CharField(max_length=100)
  age = models.IntegerField(default=10)
  lastname = models.CharField(max_length=100)
  firstname = models.CharField(max_length=100)