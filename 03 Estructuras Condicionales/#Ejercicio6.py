#Ejercicio6

#Creamos un grupo aleatorio de 50 numeros en el rango (1, 100)
import random
numeros_aleatorios = [random.randint(1, 100) for i in range (50)]

#Importamos las funciones que calculan la moda (mode), media (mean) y mediana (median) del paquete statistics
from statistics import mode, median, mean

#Definimos las variables usando las funciones importadas
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

#Revisamos el sesgo en el grupo de números según las condiciones que se cumplan
if media > mediana and mediana > moda:
    print("Hay sesgo positivo")
elif media < mediana and mediana < moda:
    print("Hay sesgo negativo")
elif media == mediana == moda:
    print("No hay sesgo")
