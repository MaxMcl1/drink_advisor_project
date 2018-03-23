from django.contrib import admin
from drinkadvisor.models import UserProfile
from drinkadvisor.models import DrinkProfile, CommentProfile

# Register your models here.

class DrinkProfileAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = (
                    'owner',
                    'name',
                    'calories',
                    'sugar',
                    'is_energy_drink',
                    'sugar_free',
                    'picture',
                    'views')

class CommentProfileAdmin(admin.ModelAdmin):
    list_display = ('drink',
                    'owner',
                    'content',
                    'rate')


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user',
                    'name',
                    'surname',
                    'picture')

admin.site.register(DrinkProfile, DrinkProfileAdmin)
admin.site.register(CommentProfile, CommentProfileAdmin)
admin.site.register(UserProfile, UserProfileAdmin)

