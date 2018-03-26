from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save
from datetime import datetime

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)


    def __str__(self):
        return self.user.username


class DrinkProfile(models.Model):
    name = models.CharField(max_length=128, unique=True)
    calories = models.IntegerField(default=0)
    sugar = models.IntegerField(default=0)
    is_energy_drink = models.BooleanField(default=False, blank=True)
    sugar_free = models.BooleanField(default=False, blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(DrinkProfile, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'drinks'

    def __str__(self):
        return self.name

class Comment(models.Model):
    drink = models.ForeignKey(DrinkProfile)
    comment = models.CharField(max_length=128)
    date = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.comment



