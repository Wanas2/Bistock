from django.db import models
from django.contrib.auth.models import AbstractUser

IS_ADMIN_CHOICES = [(True, 'Oui'), (False, 'Non')]

class User(AbstractUser):
    address = models.CharField(max_length=255, default="")
    tel = models.CharField(max_length=30, default="")
    is_admin = models.BooleanField(default=False, choices=IS_ADMIN_CHOICES, verbose_name="Admin?")

    class Meta:
        app_label = 'users'
