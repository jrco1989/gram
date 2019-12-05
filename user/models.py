from django.db import models 
from django.contrib.auth.models import User

class Profile(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE)
	website=models.URLField(max_length=150, blank=True)
	biog=models.TextField(blank=True)
	phone=models.CharField(blank=True, max_length=12)
	picture=models.ImageField(upload_to='user/imagens',blank=True, null=True)
	created=models.DateTimeField(auto_now_add=True)
	modified=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.user.username

	
	