from django.urls import path

from . import views

urlpatterns = [
    path("createList/", views.createList, name="createList"),

]