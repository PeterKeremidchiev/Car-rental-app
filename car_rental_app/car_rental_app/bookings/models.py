from django.contrib.auth import get_user_model
from django.db import models

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
