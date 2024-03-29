#middleware, django lo define como una serie de hooks y una api de bajo nivel para modificar los objetos response
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse #para poder llamar a las  urls por el nombre y tener que escribir la ruta

"""class ProfileCompletionMiddleware:  #pequeña aplicación para permitir navegar solo cuando el usuario haya ingresado su foto d eperfil y su biografia
   	def __init__(self, get_response):#procedimiento según documentación de Django.
   		self.get_response = get_response
   	def __call__(self, request):#code to be executed for each request before the view is called
	   	if not request.user.is_anonymous:  #validacióno para saber si un usuario está registrado--is_anonymoius es una propuedad que agrega el middleware
	  		profile = request.user.profile #una manera de traer los onetoonefield, campos asociados de un usuario, es decir, traemos al objeto usuario
	  		if not profile.picture or not profile.biog:
				if request.path not in [reverse('renueva'), reverse('bellachao')]:#permite ingresar en estas urls
		   			return redirect('renueva')
			response = self.get_response(request) #en caso de que no sea  ninguno de los ifs anteriores
	   		return response
"""

#CON CAPTURA DE EXCEPCION 
class ProfileCompletionMiddleware:
    #import pdb; pdb.set_trace()-
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        if not request.user.is_anonymous and not request.user.is_staff:
            try:  
              profile = request.user.profile
              #if not profile.picture or not profile.biog:
              if not profile.picture:
                  if request.path not in [reverse('user:renueva'), reverse('user:bellachao')] and not request.path.startswith('/admin/'):
                      return redirect('user:renueva')
            except (ObjectDoesNotExist):
              if request.path not in [reverse('user:renueva'), reverse('user:bellachao'),reverse('feed')]:
               return redirect ('posts:feed')

        response = self.get_response(request)
        return response

        