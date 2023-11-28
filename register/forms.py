from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


RODZAJE_PLCI = (
    ('m', 'Mężczyzna',),
    ('k', 'Kobieta',),
)

class RegisterForm(UserCreationForm):
    email = forms.EmailField();

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

# class CustomUserCreationForm(UserCreationForm):
#     plec= forms.CharField(label='Płeć', widget=forms.Select(choices=RODZAJE_PLCI))
#     zdjProfilu = forms.FileField()
#
#     class Meta:
#         model = Uzytkownicy
#         fields = UserCreationForm.Meta.fields + ('plec', 'zdjProfilu', )