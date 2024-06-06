from django.contrib.auth import get_user_model
from django.core.cache import cache
from datetime import datetime, timedelta
from django.conf import settings

from users.models import CustomUser

def get_online_users():
    online_users = []
    for user in CustomUser.objects.all():
        last_seen = cache.get(f'seen_{user.username}')
        if last_seen:
            if datetime.now() - last_seen < timedelta(seconds=settings.USER_LASTSEEN_TIMEOUT):
                online_users.append(user)
    return online_users