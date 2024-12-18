from django.apps import AppConfig
from django.contrib import admin

from users.models import User

admin.site.register(User)


class UserConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "users"
