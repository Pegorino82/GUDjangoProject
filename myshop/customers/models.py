from django.db import models

from django.contrib.auth.models import AbstractUser


class Customer(AbstractUser):
    _avatar = models.ImageField(
        upload_to='avatars/',
        null=True,
        blank=True,
    )
    birth_date = models.DateField(
        null=True,
        blank=True
    )

    @property
    def avatar(self):
        if not self._avatar:
            self._avatar = 'avatars/default.jpg'
        print('*' * 100)
        print(self._avatar)
        print('*' * 100)
        return self._avatar

    def __str__(self):
        return self.username
