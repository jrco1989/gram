from django.db import models

class User(request):
	name=models.CharField(leng_max(100))
	admin=models.Bolean(defautl = True)