from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from main.models import Znajomi

# Create your views here.

def profile(request, username):
    user = get_object_or_404(User, username=username)
    friends = Znajomi.objects.filter(idZapraszajacego=request.user.id, idZapraszanego=user.id).first()

    if friends:
        friend_status = friends.status
    else:
        friend_status = "Nieznajomi"

    user_firstname = user.first_name
    user_lastname = user.last_name
    user_date_joined = user.date_joined
    userdata = {'user_username': username, 'user_firstname': user_firstname, 'user_lastname': user_lastname, 'user_date_joined': user_date_joined, "friend_status": friend_status}
    return render(request, 'profile/profile.html', userdata)

def edit_profile(request, username):
    user = get_object_or_404(User, username=username)

    user_firstname = user.first_name
    user_lastname = user.last_name
    user_date_joined = user.date_joined
    userdata = {'user_username': username, 'user_firstname': user_firstname, 'user_lastname': user_lastname, 'user_date_joined': user_date_joined}
    return render(request, 'profile/edit.html', userdata)

def send_invite(request, username):
    invitedUser = get_object_or_404(User, username=username)

    invite = Znajomi(idZapraszajacego=invitedUser, idZapraszanego=request.user, status="Oczekujące")
    invite2 = Znajomi(idZapraszajacego=request.user, idZapraszanego=invitedUser, status="Wysłano")

    invite.save()
    invite2.save()

    return redirect("profile", username=username)

def accept_invite(request, username):
    invitedUser = get_object_or_404(User, username=username)
    invite = Znajomi.objects.filter(idZapraszajacego=request.user.id, idZapraszanego=invitedUser.id).first()
    invite2 = Znajomi.objects.filter(idZapraszajacego=invitedUser.id, idZapraszanego=request.user.id).first()

    invite.status="Przyjaciele"
    invite2.status="Przyjaciele"

    invite.save()
    invite2.save()

    return redirect("profile", username=username)

def unfriend(request, username):
    invitedUser = get_object_or_404(User, username=username)
    invite = Znajomi.objects.filter(idZapraszajacego=request.user.id, idZapraszanego=invitedUser.id).first()
    invite2 = Znajomi.objects.filter(idZapraszajacego=invitedUser.id, idZapraszanego=request.user.id).first()

    invite.delete()
    invite2.delete()

    return redirect("profile", username=username)

def password_change(request, username):
    user = get_object_or_404(User, username=username)

    user_firstname = user.first_name
    user_lastname = user.last_name
    user_date_joined = user.date_joined
    userdata = {'user_username': username, 'user_firstname': user_firstname, 'user_lastname': user_lastname, 'user_date_joined': user_date_joined}
    return render(request, 'profile/edit.html', userdata)

def avatar_change(request, username):
    user = get_object_or_404(User, username=username)

    user_firstname = user.first_name
    user_lastname = user.last_name
    user_date_joined = user.date_joined
    userdata = {'user_username': username, 'user_firstname': user_firstname, 'user_lastname': user_lastname, 'user_date_joined': user_date_joined}
    return render(request, 'profile/edit.html', userdata)