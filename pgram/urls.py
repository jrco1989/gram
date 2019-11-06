from django.contrib import admin
from django.urls import path
from pgram import views as local_v
from posts import views as posts_v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', local_v.saludo),
    path('personalizado/<str:name>/<int:age>', local_v.personalizado),
    path('post/',posts_v.list_posts)
]

