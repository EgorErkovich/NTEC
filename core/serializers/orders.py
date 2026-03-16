from rest_framework import serializers

from core.models import Order
from core.serializers.products import ProductSerializer


class OrderReadSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ("id", "product", "quantity", "status")
        read_only_fields = ("id",)


class OrderCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ("id", "product", "quantity", "status")
        read_only_fields = ("id", "status")

    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError("Количество должно быть больше 0")
        return value


class OrderStatusSerializer(serializers.Serializer):
    status = serializers.ChoiceField(choices=Order.STATUS_CHOICES)


class OrderUpdateItemsSerializer(serializers.Serializer):
    product = serializers.IntegerField(required=False)
    quantity = serializers.IntegerField(required=False, min_value=1)

    def validate(self, attrs):
        if not attrs:
            raise serializers.ValidationError("Нужно передать хотя бы одно поле")
        return attrs
