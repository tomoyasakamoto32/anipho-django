from django.urls import path
from .views import UserCreateView, UserLoginView, UserLogoutView
from . import views

app_name = "accounts"

urlpatterns = [
  path('user_create/', UserCreateView.as_view(), name='user_create'),
  path('sample/', views.sample, name='sample_user'),
  path('sample2/', views.sample2, name='sample_user2'),
  path('user_login/', UserLoginView.as_view(), name='user_login'),
  path('user_logout/', UserLogoutView.as_view(), name='user_logout'),
]