import phonenumbers
from django.core.exceptions import ValidationError
from django.db import models


def validate_phone(value):
    try:
        number = phonenumbers.parse(value, None)
        if not phonenumbers.is_valid_number(number):
            raise ValidationError("Введите корректный международный номер телефона в формате +XXXXXXXXXXX")
    except Exception:
        raise ValidationError("Введите корректный международный номер телефона в формате +XXXXXXXXXXX")


class Manufacturer(models.Model):
    name = models.CharField("Имя", max_length=255)
    country = models.CharField("Страна", max_length=255)
    phone = models.CharField(
        "Телефон",
        max_length=20,
        validators=[validate_phone]
    )

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"
        ordering = ["id"]

    def __str__(self):
        return self.name
