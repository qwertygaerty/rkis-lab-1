from django.db import models


class User(models.Model):
    avatar = models.ImageField(upload_to='media')
    username = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    password = models.CharField(max_length=250)