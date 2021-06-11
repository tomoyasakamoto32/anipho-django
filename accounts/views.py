from django.shortcuts import render
import os
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .models import User
from .forms import UserCreationForm, UserLoginForm

class UserCreateView(CreateView):
  model = User
  template_name = os.path.join('accounts', 'user_create.html')
  form_class = UserCreationForm

  success_url = reverse_lazy('accounts:sample_user')

def sample(request):
  return render(request, 'sample.html')

def sample2(request):
  return render(request, 'sample2.html')


class UserLoginView(LoginView):
  template_name = os.path.join('accounts', 'user_login.html')
  authentication_form = UserLoginForm


class UserLogoutView(LogoutView):
  pass
