from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    path("signup", views.signup, name="signup"),
    path("login",views.login, name="login"),
    path("logout",views.logout,name="logout"),
    #path('change_password', views.change_password, name='change_password'),
    ]