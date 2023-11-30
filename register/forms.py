from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

RODZAJE_PLCI = (
    ('m', 'Mężczyzna',),
    ('k', 'Kobieta',),
)

class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Nazwa użytkownika',
                               help_text='50 znaków lub mniej. Dozwolone znaki: litery, cyfry i @/./+/-/_.',
                               max_length=50)
    email = forms.EmailField
    password1 = forms.CharField(label='Nowe hasło', widget=forms.PasswordInput,
                                help_text="<ul><li>Twoje hasło nie może być podobne do loginu, bądź maila.</li>" +
                                          "<li>Twoje hasło musi składać się z co najmiej 8 znaków.</li>" +
                                          "<li>Twoje hasło nie może być powszechnie używanym hasłem.</li>" +
                                          "<li>Twoje hasło nie może składać się tylko z cyfr.</li></ul>")
    password2 = forms.CharField(label='Potwierdź nowe hasło', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        labels = {
            'email': 'E-mail',
        }

# class CustomUserCreationForm(UserCreationForm):
#     plec= forms.CharField(label='Płeć', widget=forms.Select(choices=RODZAJE_PLCI))
#     zdjProfilu = forms.FileField()
#
#     class Meta:
#         model = Uzytkownicy
#         fields = UserCreationForm.Meta.fields + ('plec', 'zdjProfilu', )
