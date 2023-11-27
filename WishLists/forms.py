# forms.py

from django import forms
from main.models import Listy

class ListyForm(forms.ModelForm):
    class Meta:
        model = Listy
        fields = ['tytul', 'opis']