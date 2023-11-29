from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.

def profile(request, username):
    user = get_object_or_404(User, username=username)

    user_firstname = user.first_name
    user_lastname = user.last_name
    user_date_joined = user.date_joined
    userdata = {'user_username': username, 'user_firstname': user_firstname, 'user_lastname': user_lastname, 'user_date_joined': user_date_joined}
    return render(request, 'profile/profile.html', userdata)