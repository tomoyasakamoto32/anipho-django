from django.shortcuts import render
import os
from django.views.generic.list import ListView
from .models import Post

class PostListView(ListView):
  model = Post
  template_name = os.path.join('posts', 'post_list.html')