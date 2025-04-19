#Semana_5 Ejercicio_9

#Definimos la funcion
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return round(fahrenheit, 2)

#Solicitamos entrada en celsius y llamamos funcion para pasar a fahrenheit
celsius = float(input("Ingrese la temperatura en celsius: "))
print("El equivalente en fahrenheit es:", celsius_a_fahrenheit(celsius))













