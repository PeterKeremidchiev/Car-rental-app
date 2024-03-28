from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from car_rental_app.cars.models import Car

UserModel = get_user_model()


class Booking(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
    car = models.OneToOneField(
        Car,
        on_delete=models.CASCADE,
    )

class Review(models.Model):
    MAX_REVIEW_LENGTH = 500
    review = models.TextField(
        max_length=500,
        null=False,
        blank=False,
    )
    rating = models.IntegerField(
        null=False,
        blank=False,
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ]
    )
    date_created = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

