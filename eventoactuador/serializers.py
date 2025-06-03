from rest_framework import serializers
from .models import EventoActuador

class EventoActuadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventoActuador
        fields = '__all__'
