from rest_framework import viewsets

from core.models import Manufacturer
from core.serializers.manufacturers import ManufacturerSerializer


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
