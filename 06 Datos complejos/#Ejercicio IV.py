#Ejercicio IV

#Diccionario vacío para los contactos
agenda = {}

#Inputs
print("Cargá 5 contactos en la agenda:")
for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto {i+1}: ")
    numero = input(f"Ingresá el número telefónico de {nombre}: ")
    agenda[nombre] = numero

#Consulta
consulta = input("\nIngresá el nombre del contacto que querés buscar: ")

if consulta in agenda:
    print(f"El número de {consulta} es {agenda[consulta]}")
else:
    print(f"No se encontró el contacto llamado {consulta}.")























