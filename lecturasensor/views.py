from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import LecturaSensor
from .serializers import LecturaSensorSerializer

class LecturaSensorListCreateView(generics.ListCreateAPIView):
    queryset = LecturaSensor.objects.all()
    serializer_class = LecturaSensorSerializer
    permission_classes = [IsAuthenticated]

class LecturaSensorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LecturaSensor.objects.all()
    serializer_class = LecturaSensorSerializer
    permission_classes = [IsAuthenticated]

