#Ejercicio2

#Solicitamos la nota al usuario
nota = float(input("Ingrese su nota por favor: "))

#Usamos un condicional para ver si aprobo o no
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#NOTA: este programa podría mejorarse usando el condicional para determinar que aprobado sea entre 6 y 10,
#desaprobado entre 0 y 6 (sin incluir), y arrojando ERROR si ingresa otro número fuera de rango (pero el ejercicio no lo pedía)
