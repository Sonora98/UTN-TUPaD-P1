#Ejercicio_recursivo_4

#definimos la funcion
def decimal_a_binario(num):
    if num == 0:
        return "0"
    elif num == 1:
        return "1"
    else:
        return decimal_a_binario(num // 2) + str(num % 2)

#Pedimos input y mostramos el resutlado
num = int(input("Ingrese un número positivo: "))
print(f"El número {num} en binario es: ", decimal_a_binario(num))






