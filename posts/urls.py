from django.urls import path
from .views import (
  PostListView, PostCreateView
)
from . import views


app_name = 'posts'

urlpatterns = [
  path('post_list/', PostListView.as_view(), name='post_list'),
  path('post_create/', views.post_create, name='post_create'),
  path('post_detail/', DetailView, name='post_create'),
]
