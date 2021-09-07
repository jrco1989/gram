from django.contrib import admin
from posts.models import Post

"""from django.contrib import admin
from .models import Post

admin.site.register(Post)""" #hace posible registrar nuestro modelo en el admin. 
# Register your models here.

# admin.site.unregister(Post)
admin.site.register(Post)
