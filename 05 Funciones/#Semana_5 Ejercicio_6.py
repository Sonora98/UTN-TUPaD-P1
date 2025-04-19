#Semana_5 Ejercicio_6

#Definimos la funcion, usamos iteracion for ya que conocemos las veces a iterar
def tabla_multiplicar(numero):
    print("La tabla de multiplicar de", numero, "es la siguiente:")
    for i in range(1, 11):
        print(numero, "x", i, "=", numero*i)

    
#Solicitamos entrada, devolvemos tabla con la funcion
numero = int(input("Ingrese un número: "))
tabla_multiplicar(numero)


















