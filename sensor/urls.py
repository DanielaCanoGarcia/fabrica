from django.urls import path
from .views import SensorListCreateView, SensorRetrieveUpdateDestroyView

urlpatterns = [
    path('', SensorListCreateView.as_view(), name='sensores'),
    path('<int:pk>/', SensorRetrieveUpdateDestroyView.as_view(), name='sensor-detail'),
]
