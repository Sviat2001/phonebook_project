import datetime
from django.utils.deprecation import MiddlewareMixin
from django.core.cache import cache
from django.conf import settings

class ActiveUserMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            now = datetime.datetime.now()
            cache.set(f'seen_{request.user.username}', now, settings.USER_LASTSEEN_TIMEOUT)
