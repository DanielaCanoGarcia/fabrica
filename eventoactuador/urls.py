from django.urls import path
from .views import EventoActuadorListCreateView, EventoActuadorRetrieveUpdateDestroyView

urlpatterns = [
    path('', EventoActuadorListCreateView.as_view(), name='eventoactuador-list'),
    path('<int:pk>/', EventoActuadorRetrieveUpdateDestroyView.as_view(), name='eventoactuador-detail'),
]
