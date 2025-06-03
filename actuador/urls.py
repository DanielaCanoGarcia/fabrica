from django.urls import path
from .views import ActuadorListCreateView, ActuadorRetrieveUpdateDestroyView

urlpatterns = [
    path('', ActuadorListCreateView.as_view(), name='actuadores'),
    path('<int:pk>/', ActuadorRetrieveUpdateDestroyView.as_view(), name='actuador-detail'),
]
