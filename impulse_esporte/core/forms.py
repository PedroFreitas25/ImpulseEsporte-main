from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    """
    Um formulário de criação de usuário com campos adicionais, se necessário.
    Por enquanto, vamos usar o padrão.
    """
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

class CustomAuthenticationForm(AuthenticationForm):
    """
    Um formulário de autenticação customizado, se necessário.
    """
    pass