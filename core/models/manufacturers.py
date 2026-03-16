from django.db import models


class Manufacturer(models.Model):
    name = models.CharField("Имя", max_length=255)
    country = models.CharField("Страна", max_length=255)
    phone = models.CharField("Телефон", max_length=50)

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"
        ordering = ["id"]

    def __str__(self):
        return self.name
