#Ejercicio10

#solicitamos las variables al usuario. Para mes usamos numeros porque reducen la sintaxis (escribir tantos nombres seria engorroso y no es necesario acá)
#Usamos funcion .strip().upper() para converitr hemisferio a mayuscula en caso de input en minuscula
hemisferio = input("Ingrese el hemisferio en el que se encuentra (N/S): ").strip().upper()
mes = int(input("Ingrese el mes actual (use números): "))
dia = int(input("Ingrese el día: "))

#Definimos 3 condicionales para marcar mensaje de ERROR en caso de que alguna de las variables no sea la correcta.
if hemisferio != "S" and hemisferio != "N":
    print("ERROR: hemisferio inválido. Solo válidas opciones 'S' o 'N'")

if mes not in range(1, 13):
    print("ERROR: mes inválido. Solo válidos número del 1 al 12")

if dia not in range(1, 32):
    print("ERROR: día inválido. Solo válido del 1 al 31")

#Anidamos condicionales
#Primero chequeamos que las variables mes y dia esten bien, sino el codigo no se ejectuta
#Luego chequeamos que haya ingresado N o S, sino el codigo no se ejecuta
#Si ingreso N, se ejecuta condicional de Hemisferio Norte; con S el de Hemisferio Sur
if mes in range(1, 13) and dia in range(1, 32):
    if hemisferio == "N":
        if mes == 1 or mes == 2 or (mes == 12 and dia in range(21, 32)) or (mes == 3 and dia in range(1, 21)):
            print("Usted se encuentra en INVIERNO")
        elif mes == 4 or mes == 5 or (mes == 3 and dia in range(21, 32)) or (mes == 6 and dia in range(1, 21)):
            print("Usted se encuentra en PRIMAVERA")
        elif mes == 7 or mes == 8 or (mes == 6 and dia in range(21, 31)) or (mes == 9 and dia in range(1, 21)):
            print("Usted se encuentra en VERANO")
        elif mes == 10 or mes == 11 or (mes == 9 and dia in range(21, 31)) or (mes == 12 and dia in range(1, 21)):
            print("Usted se encuentra en OTOÑO")
    else:
        pass
    if hemisferio == "S":
        if mes == 1 or mes == 2 or (mes == 12 and dia in range(21, 32)) or (mes == 3 and dia in range(1, 21)):
            print("Usted se encuentra en VERANO")
        elif mes == 4 or mes == 5 or (mes == 3 and dia in range(21, 32)) or (mes == 6 and dia in range(1, 21)):
            print("Usted se encuentra en OTOÑO")
        elif mes == 7 or mes == 8 or (mes == 6 and dia in range(21, 31)) or (mes == 9 and dia in range(1, 21)):
            print("Usted se encuentra en INVIERNO")
        elif mes == 10 or mes == 11 or (mes == 9 and dia in range(21, 31)) or (mes == 12 and dia in range(1, 21)):
            print("Usted se encuentra en PRIMAVERA")
    else:
        pass
else:
    pass

#OUTPUT: determinamos en que rango se encuentran los datos ingresados e imprimimos mensaje de salida con estacion correspondiente



