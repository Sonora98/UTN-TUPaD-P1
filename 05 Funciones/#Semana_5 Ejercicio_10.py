#Semana_5 Ejercicio_10

#Definimos la funcion
def calcular_promedio(a, b, c):
    prom = (a + b + c) / 3
    return round(prom, 2)


#Solicitamos los numero al usuario
a = float(input("Ingrese un primer número: "))
b = float(input("Ingrese un segundo número: "))
c = float(input("Ingrese un tercer número: "))

#Devolvemos el promedio llamando a la funcion
print(f"El promedio de {a}, {b} y {c} es:", calcular_promedio(a, b, c))



















