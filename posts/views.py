from django.shortcuts import render, redirect, get_object_or_404
import os
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post, Like
from django.http import Http404
from .forms import PostForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.timezone import make_aware
from datetime import datetime

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

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    post = kwargs['object']
    like = Like.objects.filter(post = post.pk)
    context['like_count'] = like.count()
    isLike = Like.objects.filter(post = post.pk, user=self.request.user)
    print(isLike)
    if isLike:
      context['isLike']=True
    else:
      context['isLike']=False
    return context


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


def like_create(request, pk):
  if request.method == 'POST':
    post = get_object_or_404(Post, pk=pk)
    like = Like.objects.filter(user=request.user, post=post)
    if like.exists():
      like.delete()
    else:
      like.create(user=request.user, post=post, created_at=make_aware(datetime.now()))
  return redirect('posts:post_detail', pk=pk)