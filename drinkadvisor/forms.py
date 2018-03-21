from django import forms
from django.db import models
from django.contrib.auth.models import User
from drinkadvisor.models import UserProfile, Drink




class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile

        fields = ( 'picture',)



class DrinkForm(forms.ModelForm):

    class Meta:
        model = Drink
        fields = ('name', 'picture',)



