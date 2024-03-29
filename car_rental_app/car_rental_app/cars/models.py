from django.contrib.auth import get_user_model
from django.db import models


UserModel = get_user_model()

class Car(models.Model):
    MAX_MAKE_LENGTH = 100
    MAX_MODEL_LENGTH = 100
    MAX_TRANSMISSION_LENGTH = 100
    make = models.CharField(
        max_length=MAX_MAKE_LENGTH,
    )
    model = models.CharField(
        max_length=MAX_MODEL_LENGTH,
    )
    year = models.PositiveIntegerField()
    price_per_day = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    available = models.BooleanField(
        default=True,
    )
    image = models.URLField(
        blank=True,
        null=True,
    )
    transmission = models.CharField(
        max_length=MAX_TRANSMISSION_LENGTH,
        blank=True,
        null=True,
    )
    type_of_fuel = models.CharField(
        max_length=MAX_TRANSMISSION_LENGTH,
        blank=True,
        null=True,
    )
    fuel_consumption = models.CharField(
        max_length=MAX_TRANSMISSION_LENGTH,
        blank=True,
        null=True,
    )
    booked_by = models.OneToOneField(
        UserModel,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'{self.make} {self.model}'

class CarImages(models.Model):
    image_url = models.URLField()
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        related_name='images'
    )
    class Meta:
        verbose_name_plural = 'Car Images'

    def __str__(self):
        return f"Image of {self.car.make} {self.car.model}"