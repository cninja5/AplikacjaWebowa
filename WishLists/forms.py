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
    nazwaPrezentu = forms.CharField(max_length=100, label="nazwa")
    cenaPrezentu = forms.FloatField(label="cena")
    linkDoPrezentu = forms.CharField(max_length=512, label="link do prezentu")
    class Meta:
        model = ZawartoscListy
        fields = ['nazwaPrezentu']
        labels = {
            'nazwaPrezentu': 'Nazwa prezentu'
        }