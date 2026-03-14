from rest_framework import serializers

from .models import Manufacturer, Order, Product


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ("id", "name", "country", "phone")
        read_only_fields = ("id",)

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Имя производителя не может быть пустым")
        return value

    def validate_country(self, value):
        if not value.strip():
            raise serializers.ValidationError("Страна не может быть пустой")
        return value

    def validate_phone(self, value):
        if not value.strip():
            raise serializers.ValidationError("Телефон не может быть пустым")
        return value


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "price", "discount", "final_price", "manufacturer")
        read_only_fields = ("id", "final_price")

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Название товара не может быть пустым")
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Цена должна быть больше 0")
        return value

    def validate_discount(self, value):
        if value < 0 or value > 100:
            raise serializers.ValidationError("Скидка должна быть в диапазоне 0–100%")
        return value


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
