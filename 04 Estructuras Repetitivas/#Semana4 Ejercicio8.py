#Semana4 Ejercicio8

#inciamos un contador en 1 para mostrar el progreso de los input
cont = 1
#inciamos contadores especificos
par = 0
impar = 0
pos = 0
neg = 0

#ciclo for para el rango solicitado
for i in range(0, 100):
    #en cada iteracion se pide un numero 
    num = int(input(f"{cont} - Ingrese un número: "))
    cont += 1 #contador solo con motivos de proligidad visual

    #se comprueba si el input es par, impar, positivo, negativo mediante condicional
    #vamos sumando en el contador que corresponda
    if num % 2 == 0:
        par += 1
    else:
        impar += 1

    if num > 0:
        pos += 1
    else:
        neg += 1
#fin iteracion

#Imprimimos resultados
print(f"Usted ingresó {cont-1} números, de los cuales:")
print(f"Son pares: {par}")
print(f"Son impares: {impar}")
print(f"Son positivos: {pos}")
print(f"Son negativos: {neg}")














