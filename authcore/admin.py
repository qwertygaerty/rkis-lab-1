from django.contrib import admin

from .models import User


# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['avatar', 'username', 'email', 'password', 'last_login']


admin.site.register(User, UserAdmin)
