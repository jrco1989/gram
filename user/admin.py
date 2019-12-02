from django.contrib import admin
from user.models import Profile

""" primer método para registar usuarios en andmin:
admin.site.register(profile)"""
#segundo método, el cual crea la case y se pone admin por convención
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	list_display=('pk','user','phone','website','picture')

# Register your models here.
