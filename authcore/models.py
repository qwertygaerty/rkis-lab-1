from django.conf import settings
from django.db import models

from django.contrib.auth.models import UserManager, AbstractUser, PermissionsMixin
from django.utils.translation import gettext as _
from django.utils.timezone import now


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='media')

    class Meta(AbstractUser.Meta):
        pass

