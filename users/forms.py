from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from django.db import models

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'gender', 'birth_date', 'password1', 'password2')


class CustomAuthenticationForm(AuthenticationForm):
    username = models.CharField(max_length=150)