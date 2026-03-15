from django.core.exceptions import ValidationError

from core.models import Manufacturer, Product

REQUIRED_COLUMNS = ["name", "price", "discount", "manufacturer_id"]


def validate_csv_structure(fieldnames):
    missing = [c for c in REQUIRED_COLUMNS if c not in fieldnames]
    if missing:
        raise ValidationError(f"Отсутствуют обязательные колонки: {', '.join(missing)}")


def validate_row_data(row, line):
    for col in REQUIRED_COLUMNS:
        value = row.get(col)
        if value is None or value.strip() == "":
            raise ValidationError(f"Пустое значение в колонке '{col}' (строка {line})")

    if not Manufacturer.objects.filter(id=row["manufacturer_id"]).exists():
        raise ValidationError(f"Производитель с id={row['manufacturer_id']} не существует (строка {line})")


def create_product_from_row(row, line):
    product = Product(
        name=row["name"],
        price=row["price"],
        discount=row["discount"],
        manufacturer_id=row["manufacturer_id"],
    )

    try:
        product.full_clean()
    except ValidationError as e:
        raise ValidationError(f"Ошибка модели в строке {line}: {e.message_dict}")

    product.save()
