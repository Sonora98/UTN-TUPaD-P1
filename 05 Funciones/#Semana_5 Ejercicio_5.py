#Semana_5 Ejercicio_5

#definimos la funcion que toma los segundos y devuelve las horas
def segundos_a_horas(segundos):
    minutos = segundos / 60
    horas = minutos / 60
    return horas

#Solicitamos los segundos al usuario y devolvemos las horas llamando a la funcion con el input como parametro
segundos = float(input("Ingrese la cantidad de segundos a convertir: "))
print("La cantidad de horas equivalente es:", segundos_a_horas(segundos))

























