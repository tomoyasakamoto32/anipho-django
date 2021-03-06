from django import forms
from .models import Post, Comment
from datetime import datetime
from accounts.models import User
from django.utils.timezone import make_aware

class PostForm(forms.ModelForm):

  class Meta:
    model=Post
    fields = ('picture', 'title', 'detail', 'animal_name')
    labels = {
      'picture':'ペットの写真',
      'title': '投稿のタイトル',
      'detail': '詳細',
      'animal_name': 'ペットの名前'
    }

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field in self.fields.values():
      field.widget.attrs['class'] = 'form-control'

  def save(self):
    post = super().save(commit=False)
    post.user = self.user
    post.created_at = make_aware(datetime.now())
    post.updated_at = make_aware(datetime.now())
    post.save()

  def update_save(self):
    post = super().save(commit=False)
    post.created_at = make_aware(datetime.now())
    post.updated_at = make_aware(datetime.now())
    post.save()


class CommentForm(forms.ModelForm):

  class Meta:
    model = Comment
    fields = ('content',)
    labels = {
      'content':'コメント',
    }

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field in self.fields.values():
      field.widget.attrs['class']= 'form-control'

  def save(self):
    comment = super.save(commit=False)
    comment.content
