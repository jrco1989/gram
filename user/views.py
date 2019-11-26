"""user_views"""
from django.shortcuts import render, redirect  #nos permite usar un método para renderizar los templates
from django.contrib.auth import authenticate, login, logout #importando las funciones de autenticadcion, logout de login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from user.models import profile
from django.db.utils import IntegrityError #importando el erro rque salión en cmd para poder capturarlo

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

		perfil=profile(user=user)     #una de las maneras para crear un nuevo resitro en la bse de datos, es creando un ainstancia del modelo PRofile casociandola con el usuario 
		perfil.save()
		return redirect('ingreso')
	return render(request, 'user/new.html')


