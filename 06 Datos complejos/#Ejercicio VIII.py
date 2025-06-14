#Ejercicio VIII

#Diccionario (productos: stock)
stock = {
    "manzanas": 10,
    "bananas": 5,
    "naranjas": 8
}

#Solicitar al usuario un producto
producto = input("Ingresá el nombre del producto: ").lower()

#Consultar si el producto existe
if producto in stock:
    print(f"Stock actual de {producto}: {stock[producto]}")
    
    #Agregar unidades
    unidades = int(input(f"¿Cuántas unidades querés agregar a {producto}? "))
    stock[producto] += unidades
    print(f"Nuevo stock de {producto}: {stock[producto]}")
else:
    #Producto nuevo
    unidades = int(input(f"{producto} no existe. ¿Cuántas unidades querés agregar como nuevo producto? "))
    stock[producto] = unidades
    print(f"{producto} agregado al stock con {unidades} unidades.")






