#Semana4 Ejercicio10

#pedimos numero al usuario
num = int(input("Ingresá un número: "))
#definimos numero invertido incializado en 0
num_inv = 0


while num > 0:
    digito = num % 10  #obtenemos el ultimo digito dividiendo por 10 y arrojando el resto
    num_inv = num_inv * 10 + digito #calculamos el invertido empezando por el resto obtenido y asi cada vez
    num = num // 10 #sacamos el ultimo digito ya sumado al invertido

#mostramos resultado
print(f"El número invertido: {num_inv}")



























