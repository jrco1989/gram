
from django.contrib import admin
from django.urls import path
from posts import views as posts_views
from django.conf.urls.static import static
from django.conf import settings
#from pgram import views
from user import views as users_views


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('posts/', posts_views.list_posts, name='feed'),
    path('users/ingreso/', users_views.ingreso, name='ingreso'),
    path('users/partida/', users_views.partida, name='bellachao'),
    path('users/signup/', users_views.create, name='new'),
    path('users/me/edit/', users_views.actualizar, name='renueva')
    #path ('saludo', views.saludo)
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#permite mostrar archivos de con distintos formatos gráficos
    
    