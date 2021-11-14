from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    PasswordResetForm,
    PasswordChangeForm,
    SetPasswordForm,
)
from django.core.exceptions import ValidationError

from .models import User


class LoginForm(AuthenticationForm):
    error_messages = {
        'invalid_login': (
            (
                'Нужны правильные имя пользователя и пароль.'
                ' Пароль может быть чувствителен к регистру.'
            )
        ),
    }

    username = forms.CharField(
        label='Имя пользователя или почта',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'required': 'true',
                'placeholder': '',
            }
        ),
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'required': 'true',
                'placeholder': '',
            }
        ),
    )

    def confirm_login_allowed(self, user):
        if not user.is_active:
            link_text = 'запросите новую ссылку'
            link = f'<a href="/resend-activation/">{link_text}</a>'
            msg = (
                'Этот аккаунт не активирован.\nПроверьте свою почту, куда была'
                ' отправлена ссылка активации или {}.'
            )
            raise ValidationError(msg.format(link))


class RegistrationForm(UserCreationForm):
    username = forms.RegexField(
        label='Имя пользователя',
        max_length=30,
        regex=r'^[\w.@+-]+$',
        help_text='30 символов и меньше. Только цифры, английские буквы и @/./+/-/_',
        error_messages={
            'invalid': 'Используйте только разрешённые символы',
        },
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'required': 'true',
                'autofocus': 'autofocus',
                'placeholder': '',
            }
        ),
    )

    email = forms.EmailField(
        label='Электронная почта',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'required': 'true',
                'placeholder': '',
            }
        ),
    )

    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'required': 'true',
                'placeholder': '',
            }
        ),
    )
    password2 = forms.CharField(
        label='И ещё раз пароль',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'type': 'password',
                'required': True,
                'placeholder': '',
            }
        ),
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username and User.objects.filter(username__iexact=username).exists():
            self.add_error('username', 'Имя пользователя уже занято.')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email__iexact=email).exists():
            error_text = 'Пользователь с такой почтой уже зарегистрирован.'
            raise forms.ValidationError(error_text)
        return email


class EmailForm(forms.Form):
    email = forms.EmailField(
        label='Электронная почта',
        max_length=254,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'email',
                'autofocus': 'autofocus',
            }
        ),
    )


class ResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(
        label='',
        max_length=254,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'email',
                'autofocus': 'autofocus',
            }
        ),
    )


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='Прошлый пароль',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'autofocus': 'autofocus',
            }
        ),
    )
    new_password1 = forms.CharField(
        label='Новый пароль',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )
    new_password2 = forms.CharField(
        label='Подтвердите новый пароль',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )


class SetUserPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='Новый пароль',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'autofocus': 'autofocus',
            }
        ),
    )
    new_password2 = forms.CharField(
        label='Подтвердите пароль',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )
