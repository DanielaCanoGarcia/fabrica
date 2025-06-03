from django.db import models
from subsistema.models import Subsitema

class Actuador(models.Model):
    subsistema = models.ForeignKey(Subsitema, on_delete=models.CASCADE, related_name='actuadores')
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} ({self.tipo}) - Subsistema {self.subsistema.clave_ss}"
