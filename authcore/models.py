from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import UserManager
from django.utils.translation import gettext as _
from django.utils.timezone import now

class User(AbstractBaseUser, PermissionsMixin):
    avatar = models.ImageField(upload_to='media')
    username = models.CharField(max_length=250, unique=True)
    email = models.EmailField(max_length=250, unique=True)
    password = models.CharField(max_length=250)
    last_login = models.DateTimeField(default=now, editable=False)

    is_superadmin = models.BooleanField(_('is_superadmin'), default=False)
    is_active = models.BooleanField(_('is_active'), default=True)
    is_staff = models.BooleanField(default=True)


    USERNAME_FIELD = 'username'

    objects = UserManager()

