from django.contrib import admin
from django.urls import include, path

from authcore import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("delete_user/", views.delete_user, name="delete_user"),
]
