from django import forms
from main.models import ProfilUzytkownika

class searchForUserForm(forms.Form):
    username = forms.CharField(label='Znajdź użytkownika', max_length=50)

class editAvatarForm(forms.ModelForm):
    class Meta:
        model = ProfilUzytkownika
        fields = ['avatar']