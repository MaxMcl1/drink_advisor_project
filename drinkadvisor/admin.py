from django.contrib import admin
from drinkadvisor.models import UserProfile
from drinkadvisor.models import DrinkProfile

# Register your models here.


admin.site.register(UserProfile)
admin.site.register(DrinkProfile)
