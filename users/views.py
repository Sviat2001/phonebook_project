from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.views.generic import DetailView
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from .models import CustomUser, OnlineUser
from .serializers import CustomUserSerializer, UserRegistrationSerializer, UserLoginSerializer
from .utils import get_online_users
class UserRegistrationAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

class UserLoginAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer
    queryset = CustomUser.objects.all()
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(request, username=serializer.validated_data['username'], password=serializer.validated_data['password'])
            if user:
                django_login(request, user)
                return Response({'detail': 'Login successful.', 'user': CustomUserSerializer(user).data}, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogoutAPIView(APIView):
    def post(self, request):
        django_logout(request)
        return Response({'detail': 'Logout successful.'}, status=status.HTTP_200_OK)

class UserProfileView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'profile.html'
    context_object_name = 'user'

@login_required
def index(request):
    return render(request, 'index.html')


@login_required
def online_users_view(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden('Доступ заборонено')
    online_users = get_online_users()
    return render(request, 'online_users.html', {'online_users': online_users})