from django.contrib import admin
from drinkadvisor.models import UserProfile
from drinkadvisor.models import DrinkProfile

# Register your models here.

class DrinkProfileAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(DrinkProfile, DrinkProfileAdmin)
admin.site.register(UserProfile)

