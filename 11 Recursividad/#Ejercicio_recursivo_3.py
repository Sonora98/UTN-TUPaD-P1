#Ejercicio_recursivo_3

#Definimo la funcion de potencia
def potencia(base, exponente):
    if exponente==0:
        return 1
    elif exponente==1:
        return base
    else:
        return base * potencia(base, exponente - 1)

#solicitamos base y exponente
base = int(input("Ingrese la base para el calculo de potencia: "))
exponente = int(input("Ingrese el exponenete para el calculo de potencia: "))

#Imprimimos el resultado llamando a la función
print(f"El resultado de {base} elevado a la {exponente} es: ", potencia(base,exponente))













