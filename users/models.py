from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido_pat = models.CharField(max_length=100)
    apellido_mat = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)
    puesto = models.CharField(max_length=100)
    area = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido_pat} ({self.user.username})"
