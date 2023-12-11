from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm, LoginForm


# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

            return redirect("/login")
    else:
        form = RegisterForm()
    form = RegisterForm()
    return render(response, "register/register.html", {"form": form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('/profile/' + request.user.username)
            else:
                form.add_error(None, 'Nieprawidłowa nazwa użytkownika lub hasło.')
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})
