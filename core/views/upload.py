from django.core.files.storage import default_storage
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import ImportTask
from core.serializers import UploadFileSerializer
from core.tasks import import_products_task


class UploadProductsView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    @swagger_auto_schema(
        request_body=UploadFileSerializer,
        operation_description="Загрузка CSV файла с товарами"
    )
    def post(self, request):
        serializer = UploadFileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        file = serializer.validated_data['file']
        saved_path = default_storage.save(f'uploads/{file.name}', file)

        task = ImportTask.objects.create(
            status=ImportTask.PENDING,
            task_id=""
        )

        celery_task = import_products_task.delay(saved_path, task.id)

        task.task_id = celery_task.id
        task.save()

        return Response({"task_id": task.task_id})
