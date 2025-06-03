from django.db import models
from users.models import Usuario

class Subsitema(models.Model):
    clave_ss = models.CharField(max_length=10, unique=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='subsistemas')

    def __str__(self):
        return f"{self.clave_ss} - {self.usuario.nombre} {self.usuario.apellido_pat}"
