from PIL import Image
from django import forms
from main.models import ProfilUzytkownika


class SearchForUserForm(forms.Form):
    username = forms.CharField(label='Znajdź użytkownika', max_length=50)


class EditAvatarForm(forms.ModelForm):
    class Meta:
        model = ProfilUzytkownika
        fields = ['avatar']

        def clean_picture(self):
            avatar = self.cleaned_data.get("avatar")

            if avatar:
                image = Image.open(avatar)
                width, height = image.size

                if width != 400 or height != 400:
                    raise forms.ValidationError("Awatar musi mieć rozdzielczość 400x400px!")

            return avatar
