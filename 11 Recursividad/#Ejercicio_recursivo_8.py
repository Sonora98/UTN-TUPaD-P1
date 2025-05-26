#Ejercicio_recursivo_8

#definimos la funcion
def contar_digito(numero, digito):
    if numero==0:
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)
        
    
#pedimos inputs
numero=int(input("Ingrese un número: "))
digito=int(input("Ingrese un digito: "))

#imprimimos resultado
print(f"El dígito {digito} se repite {contar_digito(numero, digito)}, veces en el numero {numero}")



