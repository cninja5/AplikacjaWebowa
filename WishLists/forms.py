# forms.py

from django import forms
from main.models import Listy, ZawartoscListy


class ListyForm(forms.ModelForm):
    class Meta:
        model = Listy
        fields = ['tytul', 'opis']
        labels = {
            'tytul': 'Nazwa listy',
            'opis': 'Opis listy'
        }
        widgets = {
            'opis': forms.Textarea(attrs={'rows': 4, 'cols': 50})
        }


class DodajPrezentDoListyForm(forms.ModelForm):
    nazwaPrezentu = forms.CharField(max_length=100, required=True, label="nazwa", widget=forms.TextInput(attrs={'class': 'addPresentsInput'}))
    cenaPrezentu = forms.FloatField(required=True, label="cena", widget=forms.NumberInput(attrs={'class': 'addPresentsInput'}))
    linkDoPrezentu = forms.CharField(max_length=512, required=False, label="link do prezentu", widget=forms.TextInput(attrs={'class': 'addPresentsInput'}))

    class Meta:
        model = ZawartoscListy
        fields = ['nazwaPrezentu', 'cenaPrezentu', 'linkDoPrezentu']
        labels = {
            'nazwaPrezentu': 'Nazwa prezentu',
            'cenaPrezentu': 'Cena prezentu',
            'linkDoPrezentu': 'Link do prezentu',
        }


