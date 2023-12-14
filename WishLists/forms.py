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
    nazwaPrezentu = forms.CharField(max_length=100, required=True, label="nazwa")
    cenaPrezentu = forms.FloatField(required=True, label="cena")
    linkDoPrezentu = forms.CharField(max_length=512, required=False, label="link do prezentu")

    class Meta:
        model = ZawartoscListy
        fields = ['nazwaPrezentu', 'cenaPrezentu', 'linkDoPrezentu']
        labels = {
            'nazwaPrezentu': 'Nazwa prezentu',
            'cenaPrezentu': 'Cena prezentu',
            'linkDoPrezentu': 'Link do prezentu',
        }
        widgets = {
            'nazwaPrezentu': forms.TextInput(attrs={'class': 'red'}),
            'cenaPrezentu': forms.NumberInput(attrs={'class': 'cena-input-class'}),
            'linkDoPrezentu': forms.TextInput(attrs={'class': 'link-input-class'}),
        }

        class DodajPrezentDoListyForm(forms.ModelForm):
            nazwaPrezentu = forms.CharField(max_length=100, required=True, label="nazwa")
            cenaPrezentu = forms.FloatField(required=True, label="cena")
            linkDoPrezentu = forms.CharField(max_length=512, required=False, label="link do prezentu")

            class Meta:
                model = ZawartoscListy
                fields = ['nazwaPrezentu', 'cenaPrezentu', 'linkDoPrezentu']
                labels = {
                    'nazwaPrezentu': 'Nazwa prezentu',
                    'cenaPrezentu': 'Cena prezentu',
                    'linkDoPrezentu': 'Link do prezentu',
                }
                widgets = {
                    'nazwaPrezentu': forms.TextInput(attrs={'class': 'red'}),
                    'cenaPrezentu': forms.NumberInput(attrs={'class': 'cena-input-class'}),
                    'linkDoPrezentu': forms.TextInput(attrs={'class': 'link-input-class'}),
                }


