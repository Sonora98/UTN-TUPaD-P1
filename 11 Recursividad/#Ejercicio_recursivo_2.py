#Ejercicio_recursivo_2

#Definimos funcion fibonacci
def fibo_rec(posicion):
    if posicion==0:
        return 0
    elif posicion==1:
        return 1
    else: 
        return fibo_rec(posicion-1)+fibo_rec(posicion-2)


#Solicitamos input al usuario
num = int(input("Ingrese un número, se calculará la serie fibonacci hasta esa posición: "))

#Usamos un ciclo for para ir del 1 al número ingresado
for i in range(0, num+1):
    print(fibo_rec(i), end=", ")














