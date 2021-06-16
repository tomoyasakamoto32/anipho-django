from django.urls import path
from .views import (
  PostListView, PostDetailView, PostDeleteView
)
from . import views


app_name = 'posts'

urlpatterns = [
  path('post_list/', PostListView.as_view(), name='post_list'),
  path('post_create/', views.post_create, name='post_create'),
  path('post_detail/<int:pk>', PostDetailView.as_view(), name='post_detail'),
  path('post_update/<int:pk>', views.post_update, name='post_update'),
  path('post_delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
]
