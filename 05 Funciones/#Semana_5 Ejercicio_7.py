#Semana_5 Ejercicio_7

#Definimos la funcion. Usamos un condicional en caso de que b == 0 para la division.
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    mult = a * b

    if b == 0:
        div = "ERROR. No se puede dividir por 0."
    else:
        div = a / b
#Devolvemos la tabla usando \n para salto de linea
    print(f"{a} + {b} = {suma}\n{a} - {b} = {resta}\n{a} * {b} = {mult}\n{a} / {b} = {div}")

#Solitiamos entradas y llamamos a la funcion
#NOTA: no hace falta pedir a y b al usuario, el ejercicio tampoco lo pide, puede llamarse directamente a la funcion y completar a y b a gusto
a = int(input("Ingrese un número: "))
b = int(input("Ingrese otro número: "))
operaciones_basicas(a, b)






















