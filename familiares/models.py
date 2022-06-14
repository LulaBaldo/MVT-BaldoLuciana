from django.db import models

# Create your models here.

class Familiares (models.Model):
    nombre = models.CharField("Nombre", max_length=30)
    edad = models.PositiveSmallIntegerField("Edad")
    fecha_nacimiento = models.DateField("Fecha de Nacimiento")
    