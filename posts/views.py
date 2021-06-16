from django.shortcuts import render, redirect, get_object_or_404
import os
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from django.http import Http404
from .forms import PostForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class PostListView(LoginRequiredMixin, ListView):
  model = Post
  template_name = os.path.join('posts', 'post_list.html')


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


def post_update(request, pk):
  post = get_object_or_404(Post, pk=pk)
  if post.user.id != request.user.id:
    raise Http404
  update_form = PostForm(request.POST or None, instance=post)
  if update_form.is_valid():
    update_form.update_save()
    return redirect('posts:post_detail', pk=pk)
  return render(request, 'posts/post_update.html', context={
    'form': update_form
  })


class PostDeleteView(DeleteView):
  template_name=os.path.join("posts", "post_delete.html")
  model = Post
  success_url = reverse_lazy('posts:post_list')
