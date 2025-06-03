from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Actuador
from .serializers import ActuadorSerializer

class ActuadorListCreateView(generics.ListCreateAPIView):
    queryset = Actuador.objects.all()
    serializer_class = ActuadorSerializer
    permission_classes = [IsAuthenticated]

class ActuadorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actuador.objects.all()
    serializer_class = ActuadorSerializer
    permission_classes = [IsAuthenticated]

