#Ejercicio_recursivo_1

#Definimos la función para calcular el factorial de un número
def factorial(num):
    if num == 0:
        return 1
    else:
        return factorial(num - 1) * num
    

#Solicitamos input al usuario
num = int(input("Ingrese un número, se calculará el factorial de 1 al número ingresado: "))

#Usamos un ciclo for para ir del 1 al número ingresado, imprimiendo el factorial con la funcion en cada iteracion
for i in range(1, num+1):
    print(f"El factorial de {i} es: ", factorial(i))


