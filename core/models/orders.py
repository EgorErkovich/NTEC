from django.core.validators import MinValueValidator
from django.db import models


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
        "core.Product",
        verbose_name="Товар",
        on_delete=models.PROTECT,
        related_name="orders"
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
