#Ejercicio X

#diccionario países/capitales
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Francia": "París",
    "Japón": "Tokyo",
    "Egipto": "El Cairo"
}


#diccionario invertido
invertido = {}
for pais, capital in paises_capitales.items():
    invertido[capital] = pais

#imprimimos
print("Diccionario invertido:")
print(invertido)



















