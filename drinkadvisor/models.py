from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import datetime


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)


    def __str__(self):
        return self.user.username

class Drink(models.Model):
    name = models.CharField(max_length=50)
    calories = models.FloatField(default = 0)
    caffeine = models.IntegerField(default=0)
    isEnergyDrink = models.BooleanField(default = False)
    isSugarFree = models.BooleanField(default = False)
    date_uploaded = models.DateField(("Date"), default=datetime.date.today)
    picture = models.ImageField(upload_to='drinks_uploaded', blank=True)
    views = models.IntegerField(default=0)
    #slug = models.SlugField(unique=True)


    class Meta:
        verbose_name_plural = 'Drinks'

    def __str__(self):
        return self.name

class Feedback(models.Model):
    drink = models.ForeignKey(Drink)
    content = models.CharField(max_length = 400)
    rate = models.IntegerField(null = True)
    date_uploaded = models.DateField(("Date"), default=datetime.date.today)


    class Meta:
        verbose_name_plural = 'Feedbacks'

    def __str__(self):
        return self.content

