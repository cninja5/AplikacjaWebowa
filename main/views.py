from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'main/base.html')


def welcome(request):
    if request.user.is_authenticated:
        return redirect('/profile/' + request.user.username)
    return render(request, 'main/welcome.html')
