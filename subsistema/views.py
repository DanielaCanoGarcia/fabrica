from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Subsitema
from .serializers import SubsitemaSerializer

class SubsitemaListCreateView(generics.ListCreateAPIView):
    queryset = Subsitema.objects.all()
    serializer_class = SubsitemaSerializer
    permission_classes = [IsAuthenticated]

class SubsitemaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subsitema.objects.all()
    serializer_class = SubsitemaSerializer
    permission_classes = [IsAuthenticated]
