#Semana4 Ejercicio9


#inciamos un contador en 1 para mostrar el progreso de los input
cont = 1
#iniciamos acumulador en 0
suma = 0

#ciclo for para el rango solicitado
for i in range(0, 100):
    #en cada iteracion se pide un numero 
    num = int(input(f"{cont} - Ingrese un número: "))
    cont += 1 #contador solo con motivos de proligidad visual
    suma += num #acumulamos la suma de los numeros

#calculamos la media
#NOTA: a cont se le resta 1 porque la incializamos en 1 por motivos de ayuda visual
media = suma / (cont - 1)

#imprimimos resultados
print(f"Usted ingresó {cont-1} números, y su media es {media}")






















