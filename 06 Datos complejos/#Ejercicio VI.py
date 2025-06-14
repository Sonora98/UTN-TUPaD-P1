#Ejercicio VI

#diccionario vacío
alumnos = {}

#inputs
for i in range(3):
    alumno = input(f"Ingrese el nombre del alumno {i+1}: ")
    nota1 = float(input(f"Ingrese la primera nota de {alumno}: "))
    nota2 = float(input(f"Ingrese la segunda nota de {alumno}: "))
    nota3 = float(input(f"Ingrese la tercera nota de {alumno}: "))
    alumnos[alumno] = (nota1, nota2, nota3)

print(alumnos)

#promedios
print("\nPromedio de cada alumno:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")





