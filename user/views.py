"""user_views"""
from django.shortcuts import render, redirect  #nos permite usar un método para renderizar los templates
from django.contrib.auth import authenticate, login, logout #importando las funciones de autenticadcion, logout de login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from user.models import Profile
from django.db.utils import IntegrityError #importando el error que salió en cmd para poder capturarlo
from user.forms import ProfileForm

def ingreso(request):
	if request.method == 'POST':
		#print ('/*-'*24)
		username= request.POST['username']
		password= request.POST['password']
		user=authenticate(request, username=username, password=password)
		if user:
			login(request, user)
			return redirect('feed') #forma de redireccionar una página 
		else:
			return render(request, 'user/ingreso.html',{'error':'invalid username and password'})
		#print (username, ': ',password )
		#print ('/*-'*24)
	return render (request, 'user/ingreso.html')

@login_required
def partida(request):
	logout(request)
	return redirect ('ingreso')
def create(request):
	#import pdb; pdb.set_trace() para ingresar en el "debouger" y realizar consultas a la bsae de datos
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['pass']
		C_pass=request.POST['pass_conf']
		if password!=C_pass:
			return render(request, 'user/new.html', {'error':'Claves erroneas'})#para crear una alerta de erorr si las claves nocinciden 
		
		try:
			user=User.objects.create_user(username=username, password=password)#para crear un usuario
		except IntegrityError: #se debe ser específico cn oel error a fin de saber si falla por otra causa 
			return render(request, 'user/new.html', {'error':'Usuario repetido'})#para evitar y mostra el error de la creaci´pon d eun usuario repetido
		user.first_name=request.POST['firstname']
		user.last_name=request.POST['lastname']
		user.email=request.POST['email']
		user.save()

		profile=Profile(user=user) #una de las maneras para crear un nuevo resitro en la bse de datos, es creando un ainstancia del modelo PRofile casociandola con el usuario 
		profile.save()
		return redirect('ingreso')
	return render(request, 'user/new.html')

@login_required
def actualizar(request):
	profile=request.user.profile #primera forma d etraer los datos 
	if request.method == 'POST':
		form =ProfileForm(request.POST, request.FILES) # se crea una instancia de profileform
		if form.is_valid():#se realiza una validación 
			print (form.cleaned_data)
			data=form.cleaned_data
			profile.website=data['website']
			profile.phone = data['phone']
			profile.biog = data['biog']
			profile.picture = data['picture']
			profile.save()

			return redirect('renueva')

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
		#prestar atención al coxtexto "para no hacer todo el "path request punto profile.user", permite tamibien tener disponicle las variables declaradas
	#return render(request,'user/edit.html') , primera forma de realizarlo



