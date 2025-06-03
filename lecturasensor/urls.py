from django.urls import path
from .views import LecturaSensorListCreateView, LecturaSensorRetrieveUpdateDestroyView

urlpatterns = [
    path('', LecturaSensorListCreateView.as_view(), name='lecturasensor-list'),
    path('<int:pk>/', LecturaSensorRetrieveUpdateDestroyView.as_view(), name='lecturasensor-detail'),
]
