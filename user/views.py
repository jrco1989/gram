"""user_views"""
from django.shortcuts import render, redirect  #nos permite usar un método para renderizar los templates
from django.contrib.auth import authenticate, login, logout #importando las funciones de autenticadcion, logout de login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls.base import reverse_lazy
from django.views.generic.edit import FormView
from user.models import Profile
from django.db.utils import IntegrityError #importando el error que salió en cmd para poder capturarlo
from user.forms import ProfileForm, CreateForm
from django.views.generic import DetailView, FormView, UpdateView
from django.contrib.auth.models import User
from django.urls import reverse #recuerde que reverse contruye una url
from posts.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
import pdb; 

#LoginRequiredMixin es un método para que sea requerido estar loqgueado en una vista 
class  UserDetailView(LoginRequiredMixin, DetailView): 
	#se debre decir cuál va a ser el query set
	#nos decie a partir de cuál CONJUNTNO de datos se van a traer los datos 
	#all() NO ESATÀ tRAYENDO todos los datos, referencia al conjuento del cual se extraen
	queryset=User.objects.all()
	#el slug es una forma de llamar a un campo de texto único 
	slug_field='username'
	#nombre de los parámetros segùn la construcción la url
	slug_url_kwarg='username'
	template_name='user/detail.html'
	context_object_name='user' #define el objeto que treamos en el template 

	#la siguiente funcion sobre escribe el get_contex_data que nos trea datos del usuario 
	# para agregar nuevos datos al contexto, en este caso, los posts del uruario
	def get_contex_data(self,**kwargs):
		#para agregar los posts que son solo del usuario que consultasmos 
		context=super().get_context_data(**kwargs)#trae el contexto oqoue ooooooubiera traído si no se huviese sobreescrito
		user=self.get_objects()
		context['posts']=Post.objects.filter(user=user).order_by('-created')
		return context


def ingreso(request):
	if request.method == 'POST':
		username= request.POST['username']
		password= request.POST['password']
		user=authenticate(request, username=username, password=password)
		if user:
			login(request, user)
			return redirect('posts:feed') #forma de redireccionar una página 
		else:
			return render(request, 'user/ingreso.html',{'error':'invalid username and password'})
		#print (username, ': ',password )
		#print ('/*-'*24)
	return render (request, 'user/ingreso.html')

"""
def create(request):#la validación debería crearse en itri archiv, no en la vista
	#import pdb; pdb.set_trace() para ingresar en el "debouger" y realizar consultas a la bsae de datos
	primera forma de validar los campos de los usuarios
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['pass']
		C_pass=request.POST['pass_conf']
		if password!=C_pass:
			return render(request, 'user/new.html', {'error':'Claves erroneas'})#para crear una alerta de erorr si las claves nocinciden 
		
		try:
			user=User.objects.create_user(username=username, password=password)#para crear un usuario
		except IntegrityError: #se debe ser específico cn oel error a fin de saber si falla por otra causa 
			return render(request, 'user/new.html', {'error':'Usuario repetido'})#para evitar y mostra el error de la creación de un usuario repetido
		user.first_name=request.POST['firstname']
		user.last_name=request.POST['lastname']
		user.email=request.POST['email']
		user.save()

		profile=Profile(user=user) #una de las maneras para crear un nuevo resitro en la bse de datos, es creando un ainstancia del modelo PRofile casociandola con el usuario 
		profile.save()
		return redirect('ingreso')
	return render(request, 'user/new.html')
	if request.method =='POST':
		form=CreateForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect ('user:ingreso')
	else:
		form =CreateForm()
	return render(
		request=request, 
		template_name='user/new.html',
		context={'form':form})

"""
#cada que se usa un FormVIEW hay q uesobreescribir el form_valid
#porque por defoult el solo redirecciona a la URL indicada
class SignupView(FormView):
	template_name = 'user/new.html'
	form_class = CreateForm
	success_url = reverse_lazy('user:ingreso')

	def form_valid(self, form):
		form.save()
		return super().form_valid(form)

@login_required
def partida(request):
	logout(request)
	return redirect ('user:ingreso')

"""
@login_required
def actualizar(request):
	profile=request.user.profile #primera forma de traer los datos 
	if request.method == 'POST':
		form =ProfileForm(request.POST, request.FILES) #se crea una instancia de profileform
		if form.is_valid():#se realiza una validación 
			#print (form.cleaned_data)
			data=form.cleaned_data
			profile.website=data['website']
			profile.phone = data['phone']
			profile.biog = data['biog']
			print(data)
			profile.picture = data['picture']
			profile.save()
			#se usa en vez de redirect porque ella no se deja construir recibiendo argumentos creo 
			url= reverse('user:detail', kwargs={'username':request.user.username})
			return redirect(url)#se modifica para cuando la url recibe argumetnos 
	else:
		form=ProfileForm()


	return render(
		request=request,
        template_name='user/edit.html',
        context={
            'profile': profile,
            'user': request.user,
            'form': form
        })
		#prestar atención al coxtexto "para no hacer todo el "path request punto profile.user",
		#permite tamibien tener disponicle las variables declaradas
	#return render(request,'user/edit.html') , primera forma de realizarlo
"""


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Update profile view."""

    template_name = 'user/edit.html'
    model = Profile
    fields = ['website', 'biog', 'phone', 'picture']

    def get_object(self):
        """Return user's profile."""
        return self.request.user.profile

    def get_success_url(self):
        """Return to user's profile."""
        username = self.object.user.username
        return reverse('user:detail', kwargs={'username': username})
