from rest_framework import serializers

from core.models import Product


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
