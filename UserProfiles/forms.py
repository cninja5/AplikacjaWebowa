from django import forms

class searchForUserForm(forms.Form):
    username = forms.CharField(label='Znajdź użytkownika', max_length=50)