from rest_framework import viewsets

from core.models import Product
from core.serializers.orders import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.refresh_from_db()

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.refresh_from_db()
