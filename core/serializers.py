from rest_framework import serializers

from .models import ImportTask


class UploadFileSerializer(serializers.Serializer):
    file = serializers.FileField()

    def validate_file(self, file):
        name = file.name.lower()

        if not name.endswith('.csv'):
            raise serializers.ValidationError("Можно загружать только CSV файлы (.csv)")

        return file


class ImportTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImportTask
        fields = ["task_id", "status", "progress", "error"]
