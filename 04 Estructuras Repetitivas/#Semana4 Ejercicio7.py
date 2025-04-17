#Semana4 Ejercicio7

#NOTA: sumamos los numeros dentro del intervalo, sin incluir los extremos, por comprension textual de la consigna
#CONSIGNA: "...calcule la suma de todos los números comprendidos entre 0 y un número entero...", pide sumar los numeros ENTRE a y b

num = int(input("Ingrese un número positivo: ")) #pedimos numero al usuario
suma = 0 #iniciamos acumulador

if num <= 0: #si no es positivo ERROR
    print("ERROR. Solo números positivos.")
else: #si es positivo entonces:
    for i in range(0, num): #iteramos en el rango 0 a numero ingresado por usuario
        suma += i #vamos sumando
    print(f"El resultado de la suma de todos los números entre 0 y {num} es: {suma}")   #imprimimos el resultado final


















