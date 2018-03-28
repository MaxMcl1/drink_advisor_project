from django.contrib import admin
from drinkadvisor.models import UserProfile
from drinkadvisor.models import DrinkProfile, Comment

# Register your models here.

class DrinkProfileAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = (
        'name',
        'calories',
        'sugar',
        'is_energy_drink',
        'sugar_free',
        'picture',
        )

class CommentProfileAdmin(admin.ModelAdmin):
    list_display = ('drink',
                    'comment',
                    'date')

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user',
                    'picture')

admin.site.register(DrinkProfile, DrinkProfileAdmin)
admin.site.register(Comment, CommentProfileAdmin)
admin.site.register(UserProfile, UserProfileAdmin)

