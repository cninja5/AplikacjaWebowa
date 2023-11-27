# forms.py

from django import forms
from main.models import Listy

class ListyForm(forms.ModelForm):
    class Meta:
        model = Listy
        fields = ['tytul', 'opis']
        labels = {
            'tytul': 'Nazwa listy',
            'opis': 'Opis listy'
        }
        widgets = {
            'opis': forms.Textarea(attrs={'rows': 4, 'cols': 50})  # Ustawienia dla pola textarea
        }