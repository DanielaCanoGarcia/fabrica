from django.db import models
from subsistema.models import Subsitema  # Importamos la relación

class Sensor(models.Model):
    subsistema = models.ForeignKey(Subsitema, on_delete=models.CASCADE, related_name='sensores')
    tipo = models.CharField(max_length=50)
    unidad = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.tipo} ({self.unidad}) - Subsistema {self.subsistema.clave_ss}"
