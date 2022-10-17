from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class User(models.Model):
    nombre = models.CharField(max_length = 30)
    apellido= models.CharField(max_length = 30)
    email = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)

    def __str__(self):
       return f'{self.nombre} {self.apellido}'
    
class Inicar(models.Model):
    email = models.CharField(max_length = 30)
    password= models.CharField(max_length = 30)
    
    