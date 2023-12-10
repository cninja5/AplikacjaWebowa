from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, SetPasswordForm
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


class CustomPasswordChangeForm(PasswordChangeForm):
    error_messages = dict(SetPasswordForm.error_messages, **{
        'password_incorrect': ("Twoje stare hasło zostało wprowadzone niepoprawnie. "
                               "Wprowadź je ponownie."),
    })
    old_password = forms.CharField(label=("Stare hasło"),
                                   widget=forms.PasswordInput)
    new_password1 = forms.CharField(label=("Nowe hasło"),
                                    help_text="<ul><li>Twoje hasło nie może być podobne do loginu, bądź maila.</li>" +
                                              "<li>Twoje hasło musi składać się z co najmiej 8 znaków.</li>" +
                                              "<li>Twoje hasło nie może być powszechnie używanym hasłem.</li>" +
                                              "<li>Twoje hasło nie może składać się tylko z cyfr.</li></ul>",
                                    widget=forms.PasswordInput)
    new_password2 = forms.CharField(label=("Potwierdź nowe hasło"),
                                    widget=forms.PasswordInput)

    def clean_old_password(self):
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise forms.ValidationError(
                self.error_messages['password_incorrect'],
                code='password_incorrect',
            )
        return old_password

    # class Meta:
    #     labels = {
    #         'new_password1': ('Nowe hasło'),
    #         'new_password2': ('Potwierdź nowe hasło'),
    #     }

    # class CustomUserCreationForm(UserCreationForm):
    #     plec= forms.CharField(label='Płeć', widget=forms.Select(choices=RODZAJE_PLCI))
    #     zdjProfilu = forms.FileField()
    #
    #     class Meta:
    #         model = Uzytkownicy
    #         fields = UserCreationForm.Meta.fields + ('plec', 'zdjProfilu', )
