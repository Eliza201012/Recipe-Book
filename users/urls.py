from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("registration/", views.registration, name="registration"),
    path("login/", auth_views.LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", views.custom_logout, name="logout"),
    path("profile/", views.profile, name="profile")
]
