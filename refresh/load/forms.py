from django import forms
from django.contrib.auth.models import User
from .models import List


class ListForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['portfolio_site', 'profile_pic']