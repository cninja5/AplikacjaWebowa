from django.urls import path

from . import views

urlpatterns = [
    path("profile/<str:username>/", views.view_profile, name="view_profile"),
    path("profile/<str:username>/friend-list/", views.view_friend_list, name="view_friend_list"),
    path("profile/<str:username>/wishlists/", views.view_wishlists, name="view_wishlists"),
    path("search-for-user/", views.search_for_user, name="search_for_user"),
    path("profile/<str:username>/edit/", views.edit_profile, name="edit_profile"),
    path("profile/<str:username>/edit/password-change/", views.password_change, name="password_change"),
    path("profile/<str:username>/edit/avatar-change/", views.avatar_change, name="avatar_change"),
    path("profile/<str:username>/invite/", views.send_invite, name="send_invite"),
    path("profile/<str:username>/accept-invite/", views.accept_invite, name="accept_invite"),
    path("profile/<str:username>/unfriend/", views.unfriend, name="unfriend"),
    path("friends-list/", views.friends_list, name="friends_list"),

]
