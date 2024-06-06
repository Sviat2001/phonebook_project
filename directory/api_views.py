from rest_framework import generics, permissions
from .models import Subscriber
from .serializers import SubscriberSerializer

class SubscriberListCreateView(generics.ListCreateAPIView):
    serializer_class = SubscriberSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Subscriber.objects.filter(user=self.request.user).order_by('last_name')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class SubscriberDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SubscriberSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Subscriber.objects.filter(user=self.request.user)