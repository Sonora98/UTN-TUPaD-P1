#Ejercicio_recursivo_6

#definimos la funcion
def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return n % 10 + suma_digitos(n//10)

#pedimos input
n=int(input("Ingrese un número: "))

#imprimimos resultado llamando a la funcion
print("La suma de los digitos del numero ingresado es: ", suma_digitos(n))














