from django.urls import path

from . import views
from register import views as v

urlpatterns = [
    path("home/", views.index, name="index"),
    path("", views.welcome, name="welcome"),
]