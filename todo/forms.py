from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Todo

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        help_texts = {
            'username': None,
        }
        labels = {
            'username': 'Username',
        }
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
        }
        error_messages = {
            'password_mismatch': ("The two password fields didn't match."),
        }
        help_texts = {
            'username': None,
        }


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title']
        labels = {
            'title': 'Title',
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
        }