from django import forms 

from posts.models import Post

class PostForm(forms.ModelForm):

	class Meta: #configuradción de la clase en general 
		model=Post
		fields=('user','profile', 'title', 'photo')
