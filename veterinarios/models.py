from sys import maxsize
from django.db import models

# Create your models here.
class Veterinario(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre
