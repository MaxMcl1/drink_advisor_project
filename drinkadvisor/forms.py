from django import forms
from django.db import models
from django.contrib.auth.models import User
from drinkadvisor.models import UserProfile, DrinkProfile
from django.contrib.auth.forms import UserCreationForm




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
                           help_text="Please enter a drink name.")
    calories = forms.CharField(max_length=128,
                           help_text="Please enter the calories")
    sugar = forms.CharField(max_length=128,
                           help_text="Please enter the sugar.")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    


    class Meta:
        model = DrinkProfile
        fields = ('name','calories','sugar','picture')

class EditProfileForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = {'username', 'email', 'password'}


   
