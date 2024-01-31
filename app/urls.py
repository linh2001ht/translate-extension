from django.urls import path
from .views import DictListAPIView, DictDetailAPIView, TransTextAPIView

urlpatterns = [
    path('dicts/', DictListAPIView.as_view(), name='dict-list'),
    path('dicts/<int:pk>/', DictDetailAPIView.as_view(), name='dict-detail'),
    path('trans-text/', TransTextAPIView.as_view(), name='trans-text'),
]
