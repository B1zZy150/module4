from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterFrom(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2' )
        widgets = {
                'username': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
                'email': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
                'password1': forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}),
                'password2': forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}),
            }