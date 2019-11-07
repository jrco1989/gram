from django import models 

class User (models.Models):
	name = charField(max_length=90)
	Admin=Boolean.models(default=True)
	 