from django.urls import path
from .views import UsuarioListCreateView, UsuarioRetrieveUpdateDestroyView

urlpatterns = [
    path('empleados/', UsuarioListCreateView.as_view(), name='empleados'),
    path('empleados/<int:pk>/', UsuarioRetrieveUpdateDestroyView.as_view(), name='empleado-detail'),
]
