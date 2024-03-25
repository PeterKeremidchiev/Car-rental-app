from django.contrib.auth import get_user_model
from django.db import models


UserModel = get_user_model()

class Car(models.Model):
    MAX_MAKE_LENGTH = 100
    MAX_MODEL_LENGTH = 100
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
    booked_by = models.OneToOneField(
        UserModel,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

