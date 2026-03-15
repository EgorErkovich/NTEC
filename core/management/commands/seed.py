import random
from decimal import Decimal

from django.core.management.base import BaseCommand
from faker import Faker

from core.models import Manufacturer, Order, Product


class Command(BaseCommand):
    help = "Generate fake data"

    def handle(self, *args, **kwargs):
        fake = Faker("ru_RU")

        # Производители
        manufacturers = []
        for _ in range(10):
            m = Manufacturer.objects.create(
                name=fake.company(),
                country=fake.country(),
                phone=fake.phone_number()
            )
            manufacturers.append(m)

        # Товары
        products = []
        for _ in range(50):
            p = Product.objects.create(
                name=fake.word().capitalize(),
                price=Decimal(str(round(random.uniform(10, 500), 2))),
                discount=Decimal(str(round(random.uniform(0, 30), 2))),
                manufacturer=random.choice(manufacturers)
            )
            products.append(p)

        # Заказы
        for _ in range(100):
            Order.objects.create(
                product=random.choice(products),
                quantity=random.randint(1, 5),
                status=random.choice(["new", "paid", "shipped", "delivered", "cancelled"])
            )

        self.stdout.write(self.style.SUCCESS("Fake data generated!"))
