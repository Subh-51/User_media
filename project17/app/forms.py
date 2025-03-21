from django import forms 
from .models import *
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        help_texts = {'username': ''}



class Profile(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['username']
