#Ejercicio7

#solicitamos el texto al usuario
texto = str(input("Ingrese una frase o palabra por favor: "))

#definimos las vocales en un conjunto
vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

#Usamos un condicional para ver si la ultima letra del string ingresado por el usuario es una vocal (osea, está en el cjto. "vocales")
#Si está, le agregamos un ! al texto e imprimimos por pantalla, sino imprimimos tal como lo ingresó
if texto[-1] in vocales:
    texto += "!"
    print(texto)
else:
    print(texto)