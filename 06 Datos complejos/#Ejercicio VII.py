#Ejercicio VII

#Conjuntos de estudiantes que aprobaron cada parcial
parcial1 = {"Ana", "Luis", "Carlos", "Sofía"}     
parcial2 = {"Sofía", "Luis", "Martín", "Lucía"}  

#Al menos un parcial (unión)
print("Aprobaron al menos un parcial:")
print(parcial1.union(parcial2))

#Ambos parciales (intersección)
print("\nAprobaron ambos parciales:")
print(parcial1.intersection(parcial2))

#Solo uno de los dos (diferencia simétrica = A solo + B solo)
solo_uno = parcial1.difference(parcial2).union(parcial2.difference(parcial1))
print("\nAprobaron solo uno de los dos:")
print(solo_uno)





















