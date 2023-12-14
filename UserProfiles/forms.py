from PIL import Image
from django import forms
from main.models import ProfilUzytkownika


class SearchForUserForm(forms.Form):
    username = forms.CharField(label='Znajdź użytkownika', max_length=50)


class EditAvatarForm(forms.ModelForm):
    class Meta:
        model = ProfilUzytkownika
        fields = ['avatar']
        labels = {
            'avatar': 'Awatar',
        }

    def __init__(self, *args, **kwargs):
        super(EditAvatarForm, self).__init__(*args, **kwargs)
        self.fields['avatar'].widget.attrs.update({'class': 'form-control EditAvatarSize'})