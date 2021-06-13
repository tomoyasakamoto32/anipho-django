from django.db import models

class Post(models.Model):
  title = models.CharField(max_length=255)
  detail = models.TextField(max_length=1000)
  animal_name = models.CharField(max_length=100)
  picture = models.FileField(upload_to='animal_name/')

  class Meta:
    db_table='Posts'

  def __str__(self):
    return self.title