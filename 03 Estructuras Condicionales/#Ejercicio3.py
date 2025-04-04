#Ejercicio3

#solicitamos al usuario que ingrese un número, que se guarda en la variable "n"
n = int(input("Ingrese un número par: "))

#Usamos el operador % que devuelve el resto, si el resto de dividir por 2 es 0, es par.
if n % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")