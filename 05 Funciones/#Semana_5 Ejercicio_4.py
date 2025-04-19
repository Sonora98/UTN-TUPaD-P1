#Semana_5 Ejercicio_4


def calcular_area_circulo(radio):
    import math
    area = math.pi * (radio ** 2)
    
    return area

def calcular_perimetro_circulo(radio):
    import math
    perimetro = 2 * math.pi * radio
    
    return perimetro

radio = int(input("Ingrese el radio del círculo: "))

while radio <= 0:
    print("ERROR. El numero debe ser mayor que 0. Pruebe de nuevo.")
    radio = int(input("Ingrese el radio del círculo: "))

if radio > 0:
    print("El área del círculo es", calcular_area_circulo(radio), "y su perímetro es", calcular_perimetro_circulo(radio))
    

















