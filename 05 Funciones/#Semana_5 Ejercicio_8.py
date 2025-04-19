#Semana_5 Ejercicio_8

#Definimos la funcion
def calcular_imc(peso, altura):
    IMC = peso / (altura ** 2)
    return round(IMC, 2)

#Pedimos input al usuario y devolvemos IMC llamando a la funcion
peso = float(input("Ingrese su peso en kilgramos: "))
altura = float(input("Ingrese su altura en metros: "))
print("Su IMC es:", calcular_imc(peso, altura))






















