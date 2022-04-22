# Modulo para mostrar lo que hay en el inventario

productos_path = "producto.txt"

def mostrar():
    with open(productos_path) as productos:
        for line in productos:
            producto = line.split(",")
            print(producto[0])
