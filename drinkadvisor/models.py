from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)


    def __str__(self):
        return self.user.username

   # def create_profile(sender, **kwargs):
      #  if kwargs['created']:
       #     user_profile = UserProfile.objects.create(user=kwargs['instance'])

   # post_save.connect(create_profile, sender=User)
    
    
    
#class DrinkProfile(models.Model):
  #  drink_name = models.CharField(max_length = 128, unique=True)
  #  calories = models.CharField(max_length = 128, unique=True)
   # sugar = models.CharField(max_length = 128, unique=True)
  #  picture = models.ImageField(upload_to='profile_images', blank=True)


    #def __str__(self):
       # return self.drink_name 


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
