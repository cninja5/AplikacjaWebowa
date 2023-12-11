from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth.models import User

RODZAJE_PLCI = (
    ('m', 'Mężczyzna',),
    ('k', 'Kobieta',),
)


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Nazwa użytkownika', max_length=50)
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "password"]


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
                                    help_text="<br>Utwórz silne i unikatowe hasło składające się z kombinacji 8 znaków: liter, cyfr i symboli.",
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
