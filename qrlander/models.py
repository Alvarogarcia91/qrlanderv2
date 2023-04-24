from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    imagen = models.ImageField(upload_to='empleados/', null=True, blank=True)

    def __str__(self):
        return self.nombre

class Registro(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    fecha_salida = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.empleado} - {self.fecha_ingreso}'

class Visitante(models.Model):
    nombre = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    motivo = models.CharField(max_length=200)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    fecha_salida = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.nombre} - {self.fecha_ingreso}'
