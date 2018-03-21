from django.contrib import admin

from drinkadvisor.models import UserProfile, Drink, Feedback

# Register your models here.

class DrinkAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'calories',
                    'caffeine',
                    'isEnergyDrink',
                    'isSugarFree',
                    'date_uploaded',
                    'picture',
                    'views')

admin.site.register(UserProfile)

admin.site.register(Drink, DrinkAdmin)
admin.site.register(Feedback)
