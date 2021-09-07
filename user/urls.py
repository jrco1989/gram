from django.urls import path 
from user import views
#from django.views.generic import TemplateView #para poder traer la vista basada en clases 

urlpatterns=[
	path(route='profile/<str:username>/',#para traer una variable 
		#view=TemplateView.as_view(template_name='user/detail.html'), #primera vista basada en clases
		view=views.UserDetailView.as_view(),
		name='detail'),
	path(route='ingreso/',view= views.ingreso, name='ingreso'),
    path(route='partida/', view=views.partida, name='bellachao'),
    #path(route='signup/', view=views.create, name='new'),
	path(
        route='signup/',
        view=views.SignupView.as_view(),
        name='new'
    ),
    #path(route='me/edit/', view=views.actualizar, name='renueva')
	path(
        route='me/edit/',
        view=views.UpdateProfileView.as_view(),
        name='renueva'
    ),
    ]