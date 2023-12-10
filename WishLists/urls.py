from django.urls import path

from . import views

urlpatterns = [
    path("createList/", views.createList, name="createList"),
    path("addPresents/<int:idList>/", views.addPresents, name="addPresents"),
    path("myLists/", views.myLists, name="myLists"),
    path('deleteList/<int:idList>/', views.deleteList, name='deleteList'),
    path('specificList/<int:idList>/', views.specificList, name='specificList'),
    path("deletePresent/<int:idList>/<int:idPrezent>/", views.deletePresent, name="deletePresent"),
    path("specificList/<int:idList>/make-reservation/<int:idGift>/", views.makeGiftReservation, name="makeGiftReservation"),
    path("specificList/<int:idList>/cancel-reservation/<int:idGift>/", views.cancelGiftReservation, name="cancelGiftReservation"),
]