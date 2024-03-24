from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'car_rental_app.accounts'

    def ready(self):
        import car_rental_app.accounts.signals
