from django.urls import path
from . import views, api_views



urlpatterns = [
    path('', views.subscriber_list, name='subscriber_list'),
    path('subscriber/<int:pk>/', views.subscriber_detail, name='subscriber_detail'),
    path('subscriber/new/', views.subscriber_new, name='subscriber_new'),
    path('subscriber/<int:pk>/edit/', views.subscriber_edit, name='subscriber_edit'),
    path('subscriber/<int:pk>/delete/', views.subscriber_delete, name='subscriber_delete'),
    path('api/subscribers/', api_views.SubscriberListCreateView.as_view(), name='subscriber-list-create'),
    path('api/subscribers/<int:pk>/', api_views.SubscriberDetailView.as_view(), name='subscriber-detail'),
]