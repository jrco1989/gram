
from django.contrib import admin
from django.urls import path, include
#from posts import views as posts_views
from django.conf.urls.static import static #handler of statics file, help us to open files 
from django.conf import settings
#from pgram import views
#from user import views as users_views


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    #path('', posts_views.list_posts, name='feed'),
    path('',include(('posts.urls','posts'),namespace='posts')), #recibe primero la ruta y luego el include para incluir  un conjunto de  urls , quien a su vezx recibe dos parámetros, el primer un atrupla que me indica en donde está el módulo y d ecuál aplicación viene y el segundo un cojunto de nombres que definen a estas urls  
    #path('post/new/',posts_views.create_post, name='poncha'),
    path ('users/',include(('user.urls','user'),namespace='user'))
    #path('users/ingreso/', users_views.ingreso, name='ingreso'),
    #path('users/partida/', users_views.partida, name='bellachao'),
    #path('users/signup/', users_views.create, name='new'),
    #path('users/me/edit/', users_views.actualizar, name='renueva')
    #path ('saludo', views.saludo)
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#permite mostrar archivos de con distintos formatos gráficos
    
    