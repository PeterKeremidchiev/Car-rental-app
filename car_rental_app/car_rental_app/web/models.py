from django.db import models

class Contact(models.Model):
    MAX_NAME_LENGTH = 100
    MAX_PHONE_LENGTH = 20
    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        null=False,
        blank=False,
    )
    email = models.EmailField(
        blank=False,
        null=False,
    )
    phone = models.CharField(
        max_length=MAX_PHONE_LENGTH,
        null=True,
        blank=True,
    )
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"