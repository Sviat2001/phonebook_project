from django.contrib.auth.models import AbstractUser
from django.contrib.sessions.models import Session
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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


class OnlineUser(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    last_activity = models.DateTimeField()

    @classmethod
    def update_user_activity(cls, user):
        user_online, created = cls.objects.get_or_create(user=user)
        user_online.last_activity = timezone.now()
        user_online.save()

    @classmethod
    def get_online_users(cls, threshold_minutes=5):
        threshold_time = timezone.now() - timezone.timedelta(minutes=threshold_minutes)
        active_sessions = Session.objects.filter(expire_date__gte=timezone.now())
        active_users_id = [session.get_decoded().get('_auth_user_id') for session in active_sessions]
        online_users = cls.objects.filter(user_id__in=active_users_id, last_activity__gte=threshold_time)
        return online_users