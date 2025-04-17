#Semana4 Ejercicio3

num1 = int(input("Ingrese un primer número entero: ")) #pedimos primer numero
num2 = int(input("Ingrese un segundo número entero: ")) #pedimos segundo numero
suma = 0 #definimos acumulador en 0

#uso condicional para sumar ordenado empezando por el numero más chico del intervalo
#también podríamos haber indicado que el primer numero ingresado debe ser menor sí o sí, pero ejercicio no aclaraba y no podedía esto
if num1 < num2: 
    num1 = num1 + 1 #sumamos +1 para que no se sume el extremo inferior del intervalo
    while num1<num2: #mientras num1<num2 estaremos dentro del intervalo, así que:
        suma += num1 #acumulamos la suma y abajo:
        num1 += 1    #aumentamos en +1 para movernos +1 espacio dentro del intervalo

    print(f"El resultado de la suma entre los número del intervalo es: {suma}")   #llego al extremo del intervalo, no debe sumarse, se termina la iteracion, imprimo resultado     

elif num1 > num2: #funciona igual que arriba, sirve para cuando num2 es el inicio del intervalo
    num2 = num2 + 1
    while num1>num2:
        suma += num2
        num2 += 1    

    print(f"El resultado de la suma entre los número del intervalo es: {suma}")        

else: #si num1 y num2 son iguales, arroja error, no hay intervalo de enteros
    print("Los número no pueden ser iguales, pruebe de nuevo")



