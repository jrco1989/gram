from django.contrib import admin
from user.models import profile

""" primer método para registar usuarios en andmin:
admin.site.register(profile)"""
#segundo método, el cual crea la case y se pone admin por convención
@admin.register(profile)
class profileAdmin(admin.ModelAdmin):
	list_display=('pk','user','phone','website','picture')

# Register your models here.
