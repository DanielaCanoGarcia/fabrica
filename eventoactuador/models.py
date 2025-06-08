from django.db import models
from actuador.models import Actuador
from users.models import Usuario

class EventoActuador(models.Model):
    MODO_CHOICES = [
        ('manual', 'Manual'),
        ('automatico', 'Automático'),
    ]

    actuador = models.ForeignKey(Actuador, on_delete=models.CASCADE, related_name='eventos')
    modo_activa = models.CharField(max_length=20, choices=MODO_CHOICES)
    accion = models.CharField(max_length=50)
    fecha = models.DateField()
    hora = models.TimeField()
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, related_name='eventos_actuador')

    def __str__(self):
        return f"{self.fecha} {self.hora} - {self.accion} ({self.modo_activa}) - Actuador {self.actuador.nombre}"
