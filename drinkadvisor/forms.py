from django import forms
from django.db import models
from django.contrib.auth.models import User
from drinkadvisor.models import UserProfile, DrinkProfile, Comment
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime




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
    name = forms.CharField(max_length=128,
                           help_text="Please enter a drink name:   ")
    calories = forms.CharField(max_length=128,
                               help_text="Please enter the number of calories per 250ml:   ")
    sugar = forms.CharField(max_length=128,
                            help_text="Please enter the sugar content in grams per 250ml (number only):")
    is_energy_drink = forms.BooleanField(help_text="Is this an energy drink?   ", required=False)
    sugar_free = forms.BooleanField(required=False, help_text="Is this drink sugar free?   ")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = DrinkProfile
        fields = ('name', 'calories', 'sugar', 'picture', 'is_energy_drink', 'sugar_free')

class EditProfileForm(UserCreationForm):

    class Meta:
        model = User
        fields = {'username', 'email', 'password'}

class CommentForm(forms.ModelForm):
    comment = forms.CharField(max_length=500, help_text="Please enter a comment: ")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Comment
        exclude = ('drink',)




