from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    CHOICE_ROLES = (
        (3, 'admin'),
        (2, 'staff'),
        (1, 'user'),
    )
    roles = models.PositiveIntegerField(choices=CHOICE_ROLES, default='1')

    def __str__(self):
        return self.username