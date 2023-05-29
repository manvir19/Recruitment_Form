from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Participant(models.Model):
    q1 = models.CharField(max_length=50 ,null=True)
    q2 = models.IntegerField()
    q3 = models.IntegerField()
    q4 = models.CharField(max_length=50,null=True)
    q5 = models.EmailField(max_length=50,null=True)
    q6 = models.CharField(max_length=50,null=True)
    q7 = models.CharField(max_length=50,null=True)
    q8 = models.CharField(max_length=50,null=True)
    

    def __str__(self):
        return self.name

