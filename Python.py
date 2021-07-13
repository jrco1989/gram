variable = "Python"
# insert a variable into string using String concatenation
print("Hello " + variable + " I'm Pytutorial")
# insert a variable into string using concatenation
print("Hello " + str(variable) + " I'm Pytutorial")
# insert a variable into string using "%" operator
insert_var = "Hello %s I'm Pytutorial"%variable
print(insert_var)

# variable
variable_1 = "Python"
variable_2 = "Django"
# insert multi variables into string using "%" operator
insert_var = "Hello %s and %s I'm Pytutorial"%(variable_1, variable_2)
#print
print(insert_var)


# variable
age = 20
# insert multi variables int into a string
insert_var = "Hello Python and Django I'm Pytutorial I'm %d years old"%age
#print
print(insert_var)


variable_1 = "Python"
variable_2 = "Django"
age = 20
# insert variables into string using format()
insert_var = "Hello {} and {} I'm Pytutorial I'm {} years old".format(variable_1, variable_2, age)
#print
print(insert_var)
# insert variables into string using f-string
insert_var = f"Hello {variable_1} and {variable_2} I'm Pytutorial I'm {age} years old"
#print
print(insert_var)
#split
insert_var.split('')
number = '10,50,30,58'
[int(i) for i in number.split(',') ]    

from math import isqrt, sqrt

isqrt(10)
sqrt(10)
divmod(6,5)

#lambda, the firts param is the parameters and the second param is the return
lambda x:  2*x
# is the same that
def double (x):
    return x*2

#python es un lenguaje interpretado y cuando un intérprete de Python lee un archivo de Python,
#primero establece algunas variables especiales. Luego ejecuta el código desde el archivo.
#el variable __name__ se establecerá como __main__ si el módulo que se está ejecutando es el programa principal.
#si el código está importando el módulo desde otro módulo, entonces el variable __name__ se establecerá en el nombre de ese módulo
if __name__ = '__main__':
    pass