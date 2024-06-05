from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .api_views import SubscriberViewSet

router = DefaultRouter()
router.register(r'subscribers', SubscriberViewSet)

urlpatterns = [
    path('', views.subscriber_list, name='subscriber_list'),
    path('subscriber/<int:pk>/', views.subscriber_detail, name='subscriber_detail'),
    path('subscriber/new/', views.subscriber_new, name='subscriber_new'),
    path('subscriber/<int:pk>/edit/', views.subscriber_edit, name='subscriber_edit'),
    path('subscriber/<int:pk>/delete/', views.subscriber_delete, name='subscriber_delete'),
    path('api/', include(router.urls)),
]