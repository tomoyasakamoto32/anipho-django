from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserChangeForm, UserCreationForm
# Register your models here.
from django.contrib.auth import get_user_model

User = get_user_model()

@admin.register(User)
class CustomizeUserAdmin(UserAdmin):
  #ユーザー編集画面で表示する要素
  fieldsets = (
    ('ユーザー情報', {'fields':('username', 'email', 'password')}),
    ('パーミッション', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
  )

  #ユーザー追加画面で表示する要素
  add_fieldsets = (
        ('ユーザー情報', {
            'fields': ('username', 'email', 'password', 'confirm_password'),
        }),
    )
  form = UserChangeForm
  add_form = UserCreationForm

  #一覧表示する要素
  list_display = ('username', 'email', 'is_active', 'is_staff')
  list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
  search_fields = ('username', 'email')
