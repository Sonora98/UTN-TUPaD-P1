#Ejercicio9

#Solicitamos al usuario la magnitud del terremoto
mag = int(input("Ingrese la magnitud del terremoto (entre 0 y 7): "))

#con un condicional, evaluamos la categoría según el rango, arrojando ERROR para número fuera del rango (menores que 0)
#al final del condicional se imprime un mensaje indicando la categoría correcta
if mag >= 0 and mag < 3:
    print('La categoría del terremoto es: "Muy leve" (imperceptible)')
elif mag >= 3 and mag < 4:
    print('La categoría del terremoto es: "Leve" (ligeramente perceptible)')
elif mag >= 4 and mag < 5:
    print('La categoría del terremoto es: "Moderado" (sentido por personas, pero generalmente no causa daños)')
elif mag >= 5 and mag < 6:
    print('La categoría del terremoto es: "Fuerte" (puede causar daños en estructuras débiles)')
elif mag >= 6 and mag < 7:
    print('La categoría del terremoto es: "Muy Fuerte" (puede causar daños significativos)')
elif mag >= 7:
    print('La categoría del terremoto es: "Extremo" (puede causar graves daños a gran escala)')
else:
    print("ERROR: Ingrese un número válido")