#TP1 Secuenciales - Alumno: Fernando Caputo

#Ejercicio1
print("Hola Mundo!")

#Ejercicio2
n2 = input("Ingrese su nombre: ")
print(f"Hola {n2}!")

#Ejercicio3
n3 = input("Ingrese su nombre: ")
a3 = input("Ingrese su apellido: ")
e3 = input("Ingrese su edad: ")
r3 = input("Ingrese su lugar de residencia: ")
print(f"Soy {n3} {a3}, tengo {e3} años y vivo en {r3}")

#Ejercicio4
radio = float(input("Ingrese el radio de un círculo: "))
pi = 3.14
area = pi * (radio * radio)
perimetro = 2 * pi * radio
print(f"El area del circulo es {area} y su perimetro es {perimetro}")

#Ejercicio5
segundos = float(input("Ingrese una cantidad de segundos: "))
horas = segundos / 60 / 60
print(f"Los segundos ingresados equivalen a {horas} hs.")

#Ejercicio6
num = int(input("Ingrese un número entero: "))
print(f"Tabla de multiplicar del {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

#Ejercicio7
num = int(input("Ingrese un número entero que no sea 0: "))
num2 = int(input("Ingrese otro número entero que no sea 0: "))
if num == 0 or num2 == 0:
    print("ERROR, usted ingresó un 0")
else:
    suma = num + num2
    resta = num - num2
    mult = num * num2
    div = num / num2
    print(f"La suma de ambos números es {suma}, la resta {resta}, la multiplicacion {mult}, y la división {div}")

#Ejercicio8
altura = float(input("Ingrese su altura en metros (incluyendo decimales)"))
peso = float(input("Ingrese su peso en kilogramos (incluyendo decimales)"))
imc = peso / (altura * altura)
print(f"Su IMC es {imc}")
     
#Ejercicio9
gr_celcius = float(input("Ingrese una temperatura en celcius: "))
gr_far = (9/5) * gr_celcius + 32
print(f"El equivalente de la temperatura ingresada en Fahrenheit es {gr_far}")

#Ejercicio10
num1 = float(input("Ingrese un primer número: "))
num2 = float(input("Ingrese un segundo número: "))
num3 = float(input("Ingrese un tercer número: "))
prom = (num1+num2+num3)/3
print(f"El promedio de los números ingresados es {prom}")


