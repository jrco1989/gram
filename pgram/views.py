from django.http import HttpResponse

from datetime import datetime 

def saludo(request):
	now=datetime.now().strftime('%dth de %b del %Y a las %H:%M hrs')
	return HttpResponse("iniciando siendo el {now}".format(now=now))

def personalizado(resquest, name, age):
	if age >18:
		message='hi {}!, welcome here'.format(name)
	else: 
		message ="hi {}!, you don't have allowed stay here".format(name)
	return HttpResponse(message)

