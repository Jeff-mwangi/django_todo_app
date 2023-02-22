from unicodedata import name
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class RegisterNewUser(UserCreationForm):
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder' :'Username', 'style': 'width: 300px;', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder' :'Email', 'style': 'width: 300px;', 'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' :'Password', 'style': 'width: 300px;', 'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' :'Password Confirmation', 'style': 'width: 300px;', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder' :'Username', 'style': 'width: 300px;', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder' :'Email', 'style': 'width: 300px;', 'class': 'form-control'}),
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile']
        widgets = {
            'image': forms.FileInput(attrs={'placeholder' :'Image', 'style': 'width: 300px;', 'class': 'form-control'}),
        }