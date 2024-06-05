from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView
from django.views.generic import DetailView

from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .models import CustomUser


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'


class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    success_url = reverse_lazy('subscriber_list')
    template_name = 'login.html'


class UserProfileView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'profile.html'
    context_object_name = 'user'