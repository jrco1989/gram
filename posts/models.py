from django.db import models
from django.contrib.auth.models import User
#from user.models import profile


"""class User (models.Model):
	name = models.CharField(max_length=90) 
	#Admin=Boolean.models(default=True)"""
class Post(models.Model):
	#user=models.ForeignKey(User, on_delete=models.CASCADE) // para borar los post cuando se borre el usuario 
	user=models.ForeignKey(User, on_delete=models.CASCADE) #models.PROTEC OR models.SET_NULL//guarda los posts despues de elimiinar el usiario (portege los datos )
	#profile=models.ForeignKey(profile, on_delete=models.CASCADE) 
	profile=models.ForeignKey('user.profile',on_delete=models.CASCADE) #otra manera de llamar el modelo profile, que evita llamar al modelo erroneo 
	title=models.CharField(max_length=89)
	photo=models.ImageField(upload_to='posts/photos')
	created=models.DateTimeField(auto_now_add=True)
	modified=models.DateTimeField(auto_now=True)

	def __str__(self): return '{}hecho por {}'.format(self.title, self.user.username)