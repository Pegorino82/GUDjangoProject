from django.db import models

from django.contrib.auth.models import AbstractUser

class Customer(AbstractUser):
    avatar = models.ImageField(
        upload_to='avatars/',
        null=True,
        blank=True
    )
    birth_date = models.DateField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.username
