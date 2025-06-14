#Ejercicio IX

#agenda
agenda = {
    ("lunes", "10:00"): "Dentista",
    ("martes", "17:00"): "Parcial Programación I",
    ("miercoles", "20:00"): "Libre",
    ("jueves", "09:00"): "Dermatólogo",
    ("viernes", "15:00"): "Libre",
    ("sabado", "07:00"): "Supermercado",
    ("domingo", "12:00"): "Libre"
}

#consulta agenda

dia = input("Ingrese un día: ")
hora = input("Ingrese la hora(hh:mm): ")

if (dia, hora) in agenda:
    print(f"El día {dia} a las {hora} usted tiene la actividad: {agenda[dia, hora]}")
else:
    print("No se registran actividades")
    



























