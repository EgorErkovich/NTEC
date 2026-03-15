from django.core.validators import MaxValueValidator, MinValueValidator
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


class Product(models.Model):
    name = models.CharField("Название", max_length=255)
    price = models.DecimalField(
        "Цена",
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    discount = models.DecimalField(
        "Скидка (%)",
        max_digits=5,
        decimal_places=2,
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )
    manufacturer = models.ForeignKey(
        Manufacturer,
        verbose_name="Производитель",
        on_delete=models.CASCADE,
        related_name='products'
    )
    final_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False, null=True, blank=True)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["id"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class Order(models.Model):

    STATUS_NEW = 'new'
    STATUS_PAID = 'paid'
    STATUS_SHIPPED = 'shipped'
    STATUS_DELIVERED = 'delivered'
    STATUS_CANCELLED = 'cancelled'

    STATUS_CHOICES = (
        (STATUS_NEW, 'Новый'),
        (STATUS_PAID, 'Оплачен'),
        (STATUS_SHIPPED, 'Отправлен'),
        (STATUS_DELIVERED, 'Доставлен'),
        (STATUS_CANCELLED, 'Отменён'),
    )

    product = models.ForeignKey(
        Product,
        verbose_name="Товар",
        on_delete=models.PROTECT,
        related_name='orders'
    )
    quantity = models.PositiveIntegerField(
        "Количество",
        default=1,
        validators=[MinValueValidator(1)]
    )
    status = models.CharField(
        "Статус",
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_NEW
    )

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ["-id"]

    def __str__(self):
        return f'Заказ #{self.id}'


class ImportTask(models.Model):
    PENDING = "pending"
    RUNNING = "running"
    SUCCESS = "success"
    FAILED = "failed"

    STATUS_CHOICES = [
        (PENDING, "Pending"),
        (RUNNING, "Running"),
        (SUCCESS, "Success"),
        (FAILED, "Failed"),
    ]

    task_id = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
    progress = models.PositiveIntegerField(default=0)
    error = models.TextField(null=True, blank=True)
