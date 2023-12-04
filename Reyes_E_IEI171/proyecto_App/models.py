from django.db import models
from django.core import validators

seleccion_sexo = [
    ("hombre", "HOMBRE"),
    ("mujer", "MUJER"),
    ("no binario", "NO BINARIO"),
]

seleccion_estado = [
    ("vigente", "VIGENTE"),
    ("suspendido","SUSPENDIDO"),
    ("retirado", "RETIRADO"),
]

class Club(models.Model):
    nombresocio = models.CharField(max_length=200, validators=[
        validators.MaxLengthValidator(80)
    ])
    fechaincorporación = models.DateField()
    añonacimiento = models.IntegerField()
    telefono = models.CharField(max_length=50)
    correo = models.EmailField()
    sexo = models.CharField(max_length=50, choices= seleccion_sexo)
    estado = models.CharField(max_length=50 ,choices= seleccion_estado)
    observacion = models.CharField(max_length=200,blank=True)