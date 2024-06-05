from django.db import models
from users.models import CustomUser


class Subscriber(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=100)
    phone_numbers = models.TextField(help_text="Separate multiple phone numbers with a comma")

    def __str__(self):
        return self.last_name