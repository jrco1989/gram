"***creation project ***"
#show date formated 
from datetime import datetime
now = datetime.now().strftime('%b %dth, %Y -/ %H:%M')

#pdb es un debbuger de python 
import pdb; pdb.set_trace()
#For to convert a dictionary of python in a JSON
import json 
data = {
    'number':'10',
    'status':'ok',
}
json.dumps(data)

"""***defniimos el método string en los modelos para iindicarle qué debe retornar al 
consultar el objeto, por default nos retorna le id ***"""
def __str__(self):
    return self.email 

""" actualizar varios registros al tiempo usando filter"""
objs = User.objects.filter(email__='xxx').update(field='new value')
