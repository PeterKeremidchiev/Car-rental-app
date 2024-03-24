from django.contrib.auth import forms as auth_forms

from car_rental_app.accounts.models import CarRentalUser


class CarRentalUserCreationForm(auth_forms.UserCreationForm):
    user = None

    class Meta(auth_forms.UserCreationForm.Meta):
        model = CarRentalUser
        fields = ('email',)