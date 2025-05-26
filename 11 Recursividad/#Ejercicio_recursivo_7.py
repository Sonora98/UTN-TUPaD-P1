#Ejercicio_recursivo_7

#definimos la funcion
def contar_bloques(n):
    if n==0:
        return 0
    else:
        return n + contar_bloques(n-1)


#solicitamos input
n=int(input("Ingrese el número de bloques del nivel más bajo: "))

#imprimimos resultado llamando a la funcion
print("Usted necesita", contar_bloques(n), "bloques para construir la piramide")









