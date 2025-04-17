#Semana4 Ejercicio4

suma = 0 #incializamos acumulador en 0
num1 = int(input("Ingrese un número entero distinto que 0: ")) #solicitamos el 1er numero

if num1 == 0: #condicional: si el input es 0 arroja mensaje de ERROR
    print("ERROR: usted ingresó el 0, pruebe de nuevo")

else: #si el input es válido (distinto que 0) ejecutamos while abajo
    while num1 != 0: #el while se ejecuta mientras el input no sea 0
        suma = suma + num1 #se acumula el último numero ingresado
        num1 = int(input("Ingrese otro número o ingrese 0 para terminar: ")) #se pide otro numero
    #al ingresar un 0 el while se detiene

    #Arrojamos el resultado acumulado. Notese la ubicacion del print, dentro del ELSE para que no se ejecute si se ingresa 0 al principio...
    #...pero fuera del WHILE para que se ejecute SOLO cuando este termine
    print(f"El resultado de la suma de los números ingresados es: {suma}")














