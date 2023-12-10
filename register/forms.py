from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

RODZAJE_PLCI = (
    ('m', 'Mężczyzna',),
    ('k', 'Kobieta',),
)

class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Nazwa użytkownika',
                               help_text='Nazwa może zawierać maksymalnie 50 znaków.',
                               max_length=50)
    first_name = forms.CharField(label='Imię', max_length=50)
    last_name = forms.CharField(label='Nazwisko', max_length=50)
    email = forms.EmailField
    password1 = forms.CharField(label='Hasło', widget=forms.PasswordInput,
                                help_text="Utwórz silne i unikatowe hasło składające się z kombinacji 8 znaków: liter, cyfr i symboli.")
    password2 = forms.CharField(label='Potwierdź hasło', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]
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
