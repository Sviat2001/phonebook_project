from users.api_views import UserLoginAPIView, UserRegistrationAPIView
from users.views import SignUpView, CustomLoginView, UserProfileView
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Phonebook API",
        default_version='v1',
        description="API documentation for the Phonebook project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@phonebook.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/register/', SignUpView.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('directory/', include('directory.urls')),
    path('accounts/profile/', UserProfileView.as_view(), name='profile'),
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/accounts/register/', UserRegistrationAPIView.as_view(), name='api-register'),
    path('api/accounts/login/', UserLoginAPIView.as_view(), name='api-login'),
]
