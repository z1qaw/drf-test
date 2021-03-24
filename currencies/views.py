from rest_framework.viewsets import ModelViewSet
from .models import Currency
from .serializers import CurrencySerializer
from rest_framework.permissions import IsAuthenticated

class CurrencyViewSet(ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = [IsAuthenticated]