#Ejercicio V

#input
frase = input("Ingrese una frase: ")

#mostramos palabras unicas (set)
print("Palabras únicas: ", set(frase.split()))

#calculamos frecuencia
frecuencia = {}
for palabra in frase:
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1

#outputs
print("\nFrecuencia de cada palabra:")
print(frecuencia)



















