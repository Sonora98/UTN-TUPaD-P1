#Semana4 Ejercicio5


import random #importamos la funcion random
num = random.randint(0, 9) #creamos un num aleatorio del 0 al 9
cont = 1 #inicializamos un contador en 1 ya que el primer intento irá por fuera del while
num_usuario = int(input("Intente adivinar el número (del 0 al 9): ")) #solicitamos al usuario que adivine, se guarda la variable

if num_usuario == num: #condicional: si acertó, mostramos cantidad de intentos
    print(f"¡Acertaste! Cantidad de intentos: {cont}")

else:
    while num_usuario != num: #si no acertó, inciamos un while, mientras no acierte:
        print("¡Equivocado!") #mensaje de que falló
        cont += 1 #sumamos un intento al contador ya que deberá intentarlo mínimo 1 vez más
        num_usuario = int(input("Intenta de nuevo: ")) #solicitamos ingrese nuevo numero y reemplazamos la variable con este nuevo input
    
    #cuando acierta, el while deja de ejecutarse y se ejecuta esta linea, que es la siguiente por fuera del while:
    print(f"¡Acertaste! Cantidad de intentos: {cont}") #indicamos cantidad de intentos final








