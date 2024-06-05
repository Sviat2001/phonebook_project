from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = models.CharField(max_length=1, choices=gender_choices)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username