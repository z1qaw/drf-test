from django.urls import path
from .views import CurrencyViewSet


urlpatterns = [
    path('currencies/', CurrencyViewSet.as_view({'get': 'list'})),
    path('currency/<int:pk>', CurrencyViewSet.as_view({'get': 'retrieve'})),
]