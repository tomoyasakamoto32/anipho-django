from django.db import models
from django.contrib.auth.models import (
  BaseUserManager, AbstractBaseUser, PermissionsMixin
)

class UserManager(BaseUserManager):

  def create_user(self, username, email=None, password=None):
    if not email:
      raise ValueError('メールアドレスを入力してください')
    user = self.model(
      username=username, 
      email=email
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self, username, email=None, password=None):
    user = self.model(
      username=username, 
      email=email
    )
    user.set_password(password)
    user.is_staff = True
    user.is_active = True
    user.is_superuser = True
    user.save(using=self._db)
    return user

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
  username = models.CharField(max_length=100)
  email = models.EmailField(max_length=255, unique=True)
  is_active = models.BooleanField(default=False)
  is_staff = models.BooleanField(default=False)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username']

  objects = UserManager()

  def __str__(self):
    return self.email