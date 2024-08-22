from django.db import models


class Car(models.Model):
    TRANSMISSION_CHOICES = [
        ("A", "Automatic"),
        ("M", "Manual"),
    ]

    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    color = models.CharField(max_length=30)
    price_per_day = models.DecimalField(max_digits=6, decimal_places=2)
    transmission = models.CharField(max_length=1, choices=TRANSMISSION_CHOICES)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
