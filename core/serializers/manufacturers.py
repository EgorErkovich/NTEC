from rest_framework import serializers

from core.models import Manufacturer


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
