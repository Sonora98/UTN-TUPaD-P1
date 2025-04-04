#Ejercicio5

#Solicitamos al usuario la contraseña con un string (cadena de caracteres)
contra = str(input("Ingrese una contraseña (debe tener entre 8 y 14 caracteres): "))

#Usamos la función len() para contar la cantidad de caracteres
#Usamos un condicional para ver que se cumplan las condiciones
if len(contra) >= 8 and len(contra) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")