from django.urls import path

from . import views

urlpatterns = [
    path("createList/", views.createList, name="createList"),
    path("addPresents/<int:idList>/", views.addPresents, name="addPresents"),

]