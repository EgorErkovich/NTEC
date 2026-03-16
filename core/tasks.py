import csv

from celery import shared_task
from django.core.exceptions import ValidationError

from core.models import ImportTask
from core.services.import_products import (create_product_from_row,
                                           validate_csv_structure,
                                           validate_row_data)


@shared_task
def import_products_task(file_path, task_db_id):
    task = ImportTask.objects.get(id=task_db_id)
    task.status = ImportTask.RUNNING
    task.progress = 0
    task.save()

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            dict_reader = csv.DictReader(f)
            fieldnames = dict_reader.fieldnames
            rows = list(dict_reader)
            total = len(rows)

            validate_csv_structure(fieldnames)

            for index, row in enumerate(rows, start=1):
                line = index + 1
                validate_row_data(row, line)
                create_product_from_row(row, line)

                task.progress = int((index / total) * 100)
                task.save()

        task.status = ImportTask.SUCCESS
        task.save()

    except ValidationError as e:
        task.status = ImportTask.FAILED
        task.error = e.messages[0]
        task.save()

    except Exception as e:
        task.status = ImportTask.FAILED
        task.error = str(e)
        task.save()
