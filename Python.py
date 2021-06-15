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

