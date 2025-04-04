#Ejercicio4

#solicitamos al usuario que ingrese su edad
edad = int(input("Ingrese su edad por favor (use 0 para menores de 1 año): "))

#usamos un condicional para indicarle al usuario su categoría según la edad ingresada.
#para esto determinamos el rango de la edad
#si se ingresa un numero menor a 0 (edad imposible), arrojamos mensaje de error
if edad >= 0 and edad < 12:
    print("Categoría: Niño/a")
elif edad >= 12 and edad < 18:
    print("Categoría: Adolescente")
elif edad >= 18 and edad < 30:
    print("Categoría: Adulto/a joven")
elif edad >= 30:
    print("Categoría: Adulto/a")
else:
    print("ERROR: edad ingresada no válida")