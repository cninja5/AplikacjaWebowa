from django.urls import path

from . import views

urlpatterns = [
    path("createList/", views.createList, name="createList"),
    path("addPresents/<int:idList>/", views.addPresents, name="addPresents"),
    path("myLists/", views.myLists, name="myLists"),
    path('deleteList/<int:idList>/', views.deleteList, name='deleteList'),
    path('specificList/<int:idList>/', views.specificList, name='specificList'),
    path("deletePresent/<int:idPrezent>/<int:idList>/", views.deletePresent, name="deletePresent"),

]