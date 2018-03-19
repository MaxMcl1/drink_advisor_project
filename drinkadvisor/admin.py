from django.contrib import admin
from drinkadvisor.models import UserProfile, Drink, Feedback

# Register your models here.


admin.site.register(UserProfile)
admin.site.register(Drink)
admin.site.register(Feedback)
