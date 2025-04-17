#Semana4 Ejercicio2

#pedimos el numero al usuario
num = int(input("Ingrese un número entero: ")) 


num = abs(num) #lo convertimos al valor absoluto (positivo)
cont = 0 #inicializamos contador en 0


if num == 0: #si se ingresa 0 el contador de dígitos se establece en 1
    cont = 1

else:
    while num > 0: #para cualquier otro numero iniciamos un ciclo while donde:
        num //= 10 #usamos //= 10 para dividir por 10, corriendo la coma un lugar a la izquierda y descartando el decimal
        cont += 1 #sumamos un dígito al contador
#de esta forma el ciclo se ejecuta hasta que queda el último dígito, que al ser divido por 10 queda "0,algo", eliminando el decimal y terminando el ciclo

print(f"El número ingresado tiene {cont} dígitos") #imprimimos el resultado







