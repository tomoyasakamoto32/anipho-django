from django.db import models
from accounts.models import User
from django.utils import timezone


class Post(models.Model):
  title = models.CharField(max_length=255)
  detail = models.TextField(max_length=1000)
  animal_name = models.CharField(max_length=100)
  picture = models.FileField(upload_to='animal_name/')
  user = models.ForeignKey(
    User, on_delete= models.CASCADE
  )
  created_at = models.DateTimeField(verbose_name="投稿日",default=timezone.now)
  updated_at = models.DateTimeField(verbose_name="更新日",default=timezone.now)

  class Meta:
    db_table='Posts'

  def __str__(self):
    return self.title


class Like(models.Model):
  post = models.ForeignKey(
    Post, on_delete=models.CASCADE
  )
  user = models.ForeignKey(
    User, on_delete=models.CASCADE
  )
  created_at = models.DateTimeField(default=timezone.now)

  class Meta:
    db_table='Likes'