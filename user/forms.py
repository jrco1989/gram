from django import forms


class ProfileForm(forms.Form):
	website=forms.URLField(max_length=200, required=True)
	biog=forms.CharField(max_length=500, required=False)
	phone=forms.CharField(max_length=20, required=False)
	picture=forms.ImageField()
