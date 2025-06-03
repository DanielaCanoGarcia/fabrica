from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import EventoActuador
from .serializers import EventoActuadorSerializer

class EventoActuadorListCreateView(generics.ListCreateAPIView):
    queryset = EventoActuador.objects.all()
    serializer_class = EventoActuadorSerializer
    permission_classes = [IsAuthenticated]

class EventoActuadorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EventoActuador.objects.all()
    serializer_class = EventoActuadorSerializer
    permission_classes = [IsAuthenticated]

