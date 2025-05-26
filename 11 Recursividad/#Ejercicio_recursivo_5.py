#Ejercicio_recursivo_5

#definimos la funcion
def es_palindromo(palabra):
    if len(palabra)==0 or len(palabra)==1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])

#solicitamos input
palabra = input("Ingrese una palabra (sin espacios ni tildes): ").lower()

#Llamamos a la funcion para ver si es o no palindromo
if es_palindromo(palabra):
    print("La palabra ingresada es un palíndromo.")
else:
    print("La palabra ingresada no es un palíndromo.")















