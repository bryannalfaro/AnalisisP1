#Universidad del Valle de Guatemala
#Analisis de Algoritmos
#Integrantes:
#Bryann Alfaro
#Diego de Jesus
#Julio Herrera
#Jose Ponce
#Gabriel Quiroz

#Referencia
#https://www.geeksforgeeks.org/nested-lambda-function-in-python/#:~:text=In%20Python%2C%20anonymous%20function%20means,is%20called%20Nested%20Lambda%20Function
#https://riptutorial.com/python/example/16723/recursive-lambda-using-assigned-variable

f = lambda x: x+1
g = lambda x: 2*x
h = lambda x: lambda y: x**2+y**2

#Sin lambdas de parametros
cero = lambda f: lambda x: x
uno = lambda f: lambda x: f(x)
dos = lambda f: lambda x: f(f(x))
tres = lambda f: lambda x: f(f(f(x)))

sucesor = lambda n: lambda f: lambda x: f(n(f)(x))

suma = lambda a: lambda b: lambda f: lambda x: a(f)(b(f)(x))
print('cero + uno + 1 = ', suma(cero)(uno)(f)(1))
print('cero + dos + 1 = ', suma(cero)(dos)(f)(1))
print('uno + cero + 5 = ', suma(uno)(cero)(f)(5))
print('dos + dos + 0 = ', suma(dos)(dos)(f)(0))
print('dos + tres + 1 = ', suma(dos)(tres)(f)(1))
print('tres + tres + 1 = ', suma(tres)(tres)(f)(1))

multiplicacion = lambda a: lambda b: lambda f: lambda x: a(b(f))(x)
print('cero * dos = ', multiplicacion(cero)(dos)(f)(0))
print('uno * dos = ', multiplicacion(uno)(dos)(f)(0))
print('dos * tres = ', multiplicacion(dos)(tres)(f)(0))
print('tres * tres = ', multiplicacion(tres)(tres)(f)(0))
