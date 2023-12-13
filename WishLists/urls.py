from django.urls import path

from . import views

urlpatterns = [
    path("createList/", views.createList, name="createList"),
    path("edit-list/<int:idList>/", views.edit_list, name="edit_list"),
    path("edit-list/<int:idList>/add-present/", views.add_present, name="add_present"),
    path("myLists/", views.myLists, name="myLists"),
    path("my-reservations/", views.myGiftReservations, name="myGiftReservations"),
    path("friendsLists/", views.friendsLists, name="friendsLists"),
    path('deleteList/<int:idList>/', views.deleteList, name='deleteList'),
    path('specificList/<int:idList>/', views.specificList, name='specificList'),
    path("deletePresent/<int:idList>/<int:idPrezent>/", views.deletePresent, name="deletePresent"),
    path("specificList/<int:idList>/make-reservation/<int:idGift>/", views.makeGiftReservation, name="makeGiftReservation"),
    path("specificList/<int:idList>/cancel-reservation/<int:idGift>/", views.cancelGiftReservation, name="cancelGiftReservation"),
]