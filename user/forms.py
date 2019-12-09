from django import forms


class Createform (forms.Form):
	usernam= forms.CharField(min_length=4, max_length=50)
	password=forms.CharField(max_length=50 widget=form.PasswordInput())
	password_confirmation=forms.CharField(max_length=69, widget=PasswordInput())
	first_name=forms.CharField(min_length=3, max_length=90 )
	last_name=forms.CharField(min_length=3, max_length=90 )
	email=forms.CharField(min_length=6, max_length=70, widget=forms.EmailInput())

	# los widgets son una representación de django de elementos de html y pueden iclluir ciertas validaciones 


class ProfileForm(forms.Form):
	website=forms.URLField(max_length=200, required=True)
	biog=forms.CharField(max_length=500, required=False)
	phone=forms.CharField(max_length=20, required=False)
	picture=forms.ImageField()
