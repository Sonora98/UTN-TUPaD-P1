#Semana_5 Ejercicio_3

#Defino la funcion, que devuelve un string
def informacion_personal(nombre, apellido, edad, residencia):
    return f'Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}'

#Solicito datos al usuario
nom = str(input("Ingrese su nombre: "))
apell = str(input("Ingrese su apellido: "))
edad = int(input("Ingrese su edad: "))
resid = str(input("Ingrese su lugar de residencia: "))

#Uso un print para imprimir el string que devuelve la funcion
print(informacion_personal(nom, apell, edad, resid))
















