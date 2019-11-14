
from django.contrib import admin
from django.urls import path
from posts import views as posts_views
from django.conf.urls.static import static
from django.conf import settings
from pgram import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path ('posts/', posts_views.list_posts),
    #path ('saludo', views.saludo)
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#permite mostrar archivos de con distintos formatos gráficos
    