from rest_framework import viewsets

from core.models import Product
from core.serializers.orders import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
