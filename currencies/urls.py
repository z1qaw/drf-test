from django.urls import path
from .views import CurrencyViewSet
from rest_framework.authtoken import views

urlpatterns = [
    path('currencies/', CurrencyViewSet.as_view({'get': 'list'})),
    path('currency/<int:pk>', CurrencyViewSet.as_view({'get': 'retrieve'})),
    path('api-token-auth/', views.obtain_auth_token)
]