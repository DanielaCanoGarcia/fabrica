from django.urls import path
from .views import SubsitemaListCreateView, SubsitemaRetrieveUpdateDestroyView

urlpatterns = [
    path('', SubsitemaListCreateView.as_view(), name='subsistemas'),
    path('<int:pk>/', SubsitemaRetrieveUpdateDestroyView.as_view(), name='subsistema-detail'),
]
