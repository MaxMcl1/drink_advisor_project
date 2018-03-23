from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length= 50)
    surname = models.CharField(max_length = 50)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def save(self, *args, **kwargs):
        super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username


class DrinkProfile(models.Model):
    owner = models.ForeignKey(UserProfile, on_delete= models.CASCADE)
    name = models.CharField(max_length=128, unique=True)
    calories = models.FloatField(default=0)
    sugar = models.FloatField(default=0)
    is_energy_drink = models.BooleanField(default=False, blank=True)
    sugar_free = models.BooleanField(default=False, blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    views = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(DrinkProfile, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'drinks'

    def __str__(self):
        return self.name

class CommentProfile(models.Model):
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    drink = models.ForeignKey(DrinkProfile, on_delete= models.CASCADE)
    content = models.TextField(default='')
    rate = models.IntegerField(null=True)


    def save(self, *args, **kwargs):
        super(CommentProfile, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'comments'


