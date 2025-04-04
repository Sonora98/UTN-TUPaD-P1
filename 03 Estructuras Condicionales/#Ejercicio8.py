#Ejercicio8

#solitiamos al usuario que ingrese su nombre
#luego solicitamos que seleccione una opcion
nombre = str(input("Ingrese su nombre: "))
opcion = int(input("Ingrese: " \
"1 (para nombre en mayúscula); " \
"2 (para nombre en minúscula); " \
"3 (para solo primera letra mayúscula): "))

#si la variable "opcion" guardo "1", la funcion upper transforma el nombre en mayuscula
#si guardo "2", la funcion lower transforma el nombre en minuscula
#si guardo "3", la funcion title transforma la primera letra de cada palabra en mayuscula
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Numero ingresado incorrecto")

#Se imprime el texto resultado