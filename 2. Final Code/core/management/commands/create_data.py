from django.core.management.base import BaseCommand
from core.models import Car
from django.utils.crypto import get_random_string
import random


class Command(BaseCommand):
    help = "Populates the database with 25 sample cars"

    def handle(self, *args, **kwargs):
        makes = ["Toyota", "Honda", "Ford", "Chevrolet", "Nissan"]
        models = ["Sedan", "SUV", "Hatchback", "Truck", "Coupe"]
        colors = ["Red", "Blue", "White", "Black", "Silver"]

        for _ in range(25):
            car = Car(
                make=random.choice(makes),
                model=f"{random.choice(models)} {get_random_string(3, '1234567890').upper()}",
                year=random.randint(2015, 2024),
                color=random.choice(colors),
                price_per_day=round(random.uniform(50, 200), 2),
                transmission=random.choice(["A", "M"]),
                is_available=random.choice([True, False]),
            )
            car.save()

        self.stdout.write(self.style.SUCCESS("Successfully created 25 sample cars"))
