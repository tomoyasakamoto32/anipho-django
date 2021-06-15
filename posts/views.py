from django.shortcuts import render, redirect
import os
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class PostListView(LoginRequiredMixin, ListView):
  model = Post
  template_name = os.path.join('posts', 'post_list.html')

class PostCreateView(CreateView):
  template_name = os.path.join('posts','post_create.html')
  form_class = PostForm

  success_url =reverse_lazy('posts:post_list')

  def form_valid(self, form):
    form.user = self.request.user
    return super().form_valid(form)


def post_create(request):
  post_form = PostForm(request.POST or None, request.FILES or None)
  if post_form.is_valid():
    post_form.user = request.user
    post_form.save()
    return redirect('posts:post_list')
  return render(request, 'posts/post_create.html', context={
      'form': post_form
    })

class PostDetailView(DetailView):
  template_name= os.path.join('posts', 'post_detail.html')
  model = Post