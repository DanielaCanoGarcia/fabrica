from django.db import models
from sensor.models import Sensor  # Importamos el modelo Sensor

class LecturaSensor(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='lecturas')
    valor = models.JSONField()  # Guardamos un array o lista en formato JSON
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"Lectura {self.id} - Sensor {self.sensor.id} - {self.fecha} {self.hora}"
