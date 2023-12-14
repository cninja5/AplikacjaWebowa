from io import BytesIO

from PIL import Image
from django.contrib.auth import update_session_auth_hash
from django.core.files.base import ContentFile
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from main.models import Znajomi, Listy, ProfilUzytkownika

from django.db.models import Subquery, Count
from django.contrib.auth.decorators import login_required

from register.forms import CustomPasswordChangeForm
from .forms import SearchForUserForm, EditAvatarForm
from django.contrib import messages


# Create your views here.

def get_common_user_data(request, username, view_friend_list=False, view_wishlists=False):
    user = get_object_or_404(User, username=username)
    friends = Znajomi.objects.filter(idZapraszajacego=request.user.id, idZapraszanego=user.id).first()

    podzapytanie = Znajomi.objects.filter(idZapraszajacego=user.id, status="Przyjaciele").values('idZapraszanego')

    profile_picture = ProfilUzytkownika.objects.filter(user_id=user.id).first()
    if profile_picture is None:
        profile_picture = 'default_profile_pic.jpg'
    else:
        profile_picture = profile_picture.avatar

    wishlists = Listy.objects.filter(loginWlasciciel=user).annotate(
        ilosc_pozycji=Count('zawartosclisty')).order_by('-id')

    friendsList = User.objects.filter(id__in=Subquery(podzapytanie)).select_related('profiluzytkownika')

    friends_count = Znajomi.objects.filter(idZapraszajacego=user.id, status="Przyjaciele").count()

    lists_count = Listy.objects.filter(loginWlasciciel=user).count()

    if friends:
        friend_status = friends.status
    else:
        friend_status = "Nieznajomi"

    user_date_joined = user.date_joined

    userdata = {
        'user_username': username,
        'user_first_name': user.first_name,
        'user_last_name': user.last_name,
        'user_date_joined': user_date_joined,
        "friend_status": friend_status,
        "friendsList": friendsList,
        "friends_count": friends_count,
        "lists_count": lists_count,
        "avatar_url": profile_picture,
        'viewFriendList': view_friend_list,
        'wishlists': wishlists,
        'viewWishLists': view_wishlists,
    }

    return userdata


def view_profile(request, username):
    userdata = get_common_user_data(request, username, view_friend_list=False, view_wishlists=False)
    return render(request, 'profile/profile.html', userdata)


def view_friend_list(request, username):
    userdata = get_common_user_data(request, username, view_friend_list=True, view_wishlists=False)
    return render(request, 'profile/profile.html', userdata)


def view_wishlists(request, username):
    userdata = get_common_user_data(request, username, view_friend_list=False, view_wishlists=True)
    return render(request, 'profile/profile.html', userdata)


@login_required
def edit_profile(request, username):
    user = get_object_or_404(User, username=username)

    profile_picture = ProfilUzytkownika.objects.filter(user_id=user.id).first()

    if profile_picture is None:
        profile_picture = 'default_profile_pic.jpg'
    else:
        profile_picture = profile_picture.avatar

    user_firstname = user.first_name
    user_lastname = user.last_name
    user_date_joined = user.date_joined
    userdata = {'edit': None, 'user_username': username, 'user_firstname': user_firstname,
                'user_lastname': user_lastname,
                'user_date_joined': user_date_joined, "avatar_url": profile_picture}
    return render(request, 'profile/edit.html', userdata)


@login_required
def password_change(request, username):
    user = get_object_or_404(User, username=username)

    profile_picture = ProfilUzytkownika.objects.filter(user_id=user.id).first()
    if profile_picture is None:
        profile_picture = 'default_profile_pic.jpg'
    else:
        profile_picture = profile_picture.avatar

    edit = "Zmiana hasła"
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Twoje hasło zostało pomyślnie zmienione!')
            return redirect('/profile/' + request.user.username + '/edit/')
    else:
        form = CustomPasswordChangeForm(request.user)

    user_date_joined = user.date_joined
    userdata = {'user_date_joined': user_date_joined, 'form': form, 'edit': edit, 'avatar_url': profile_picture}
    return render(request, 'profile/edit.html', userdata)


def crop_avatar(image):
    img = Image.open(image)

    width, height = img.size

    min_dimension = min(width, height)

    left = (width - min_dimension) / 2
    top = (height - min_dimension) / 2
    right = (width + min_dimension) / 2
    bottom = (height + min_dimension) / 2

    img = img.crop((left, top, right, bottom))

    img_io = BytesIO()
    img.save(img_io, format='JPEG')
    img_file = ContentFile(img_io.getvalue(), name=image.name)

    return img_file


@login_required
def avatar_change(request, username):
    user = get_object_or_404(User, username=username)
    user_date_joined = user.date_joined

    profile_picture = ProfilUzytkownika.objects.filter(user_id=user.id).first()
    if profile_picture is None:
        profile_picture = 'default_profile_pic.jpg'
    else:
        profile_picture = profile_picture.avatar

    edit = "Zmiana awatara"
    profil, created = ProfilUzytkownika.objects.get_or_create(user_id=user.id)

    if request.method == 'POST':
        form = EditAvatarForm(request.POST, request.FILES, instance=profil)
        if form.is_valid():
            form.instance.user = request.user

            avatar = form.cleaned_data.get('avatar')
            if avatar:
                form.instance.avatar = crop_avatar(avatar)

            form.save()
            return redirect('/profile/' + request.user.username + '/edit/')
    else:
        form = EditAvatarForm()

    userdata = {'edit': edit, 'user_username': username, 'user_date_joined': user_date_joined, 'form': form,
                'avatar_url': profile_picture}
    return render(request, 'profile/edit.html', userdata)


def search_for_user(request):
    if request.method == 'POST':
        form = SearchForUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            if User.objects.filter(username=username).exists():
                return redirect('view_profile', username=username)
            else:
                return render(request, 'profile/search_for_user.html',
                              {'form': form, 'warning': 'Podany użytkownik nie istnieje!'})
    else:
        form = SearchForUserForm()
    return render(request, 'profile/search_for_user.html', {'form': form})


@login_required
def send_invite(request, username):
    invitedUser = get_object_or_404(User, username=username)

    invite = Znajomi(idZapraszajacego=invitedUser, idZapraszanego=request.user, status="Oczekujące")
    invite2 = Znajomi(idZapraszajacego=request.user, idZapraszanego=invitedUser, status="Wysłano")

    invite.save()
    invite2.save()

    return redirect("view_profile", username=username)


@login_required
def accept_invite(request, username):
    invitedUser = get_object_or_404(User, username=username)

    invite = Znajomi.objects.filter(idZapraszajacego=request.user.id, idZapraszanego=invitedUser.id).first()
    invite2 = Znajomi.objects.filter(idZapraszajacego=invitedUser.id, idZapraszanego=request.user.id).first()

    invite.status = "Przyjaciele"
    invite2.status = "Przyjaciele"

    invite.save()
    invite2.save()

    return redirect("view_profile", username=username)


@login_required
def unfriend(request, username):
    invitedUser = get_object_or_404(User, username=username)
    invite = Znajomi.objects.filter(idZapraszajacego=request.user.id, idZapraszanego=invitedUser.id).first()
    invite2 = Znajomi.objects.filter(idZapraszajacego=invitedUser.id, idZapraszanego=request.user.id).first()

    invite.delete()
    invite2.delete()

    return redirect("friends_list")


def friends_list(request):
    podzapytanie = Znajomi.objects.filter(idZapraszajacego=request.user.id, status="Przyjaciele").values(
        'idZapraszanego')

    friendsList = User.objects.filter(id__in=Subquery(podzapytanie)).select_related('profiluzytkownika')
    return render(request, 'friends/friends_list.html', {'znajomi': friendsList})

def view_friend_invites(request):
    return render(request, 'friends/friend_invites.html')