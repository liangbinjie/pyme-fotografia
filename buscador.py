"""
Modulo para hacer busqueda dentro del inventario

"""

from os import system

inventario_path = "txt/inventario.txt"
results_path = "txt/result.txt"


# Funcion para escribir dentro de un archivo de texto
def txt(info):
    with open(results_path, 'w') as result:
        result.write(info)


# Funcion para hacer una busqueda general
def bgeneral(producto):
    encontrado = 0 # variable que nos dira si encontramos o no el producto
    # vamos a abrir el archivo plano donde estan almacenados los productos
    with open(inventario_path) as inventario:
        for linea in inventario: # por cada linea que tiene el archivo plano
            datos = linea.split(",") # dividiremos los datos que tiene cada linea

            if producto == datos[0] or producto == datos[1]: # si el nombre del producto esta dentro de la linea
                encontrado = 1 # al cambiar a uno, significa que encontramos el producto y retornamos los resultados
                return f"\nNombre de producto: {datos[0]}\nCodigo: {datos[1]}\nPrecio: {datos[2]}\nEn inventario: {datos[3]}"  # regresamos el nombre, codigo y precio del producto

    if encontrado == 0: # si no encontramos el producto, la variable se mantendra en 0 y retornamos que no lo encontramos
        return "Producto no encontrado"


# Funcion para hacer una busqueda por medio de codigo
def bcodigo1(codigo):
    encontrado = 0
    # vamos a abrir el archivo plano donde estan almacenados los productos
    with open(inventario_path) as inventario:
        for linea in inventario: # por cada linea que tiene el archivo plano
            datos = linea.split(",") # vamos a dividir los datos de cada linea dentro de un arreglo

            if codigo == datos[1]: # si el codigo del producto esta dentro de la linea
                encontrado = 1
                return f"Nombre producto: {datos[0]}\nPrecio: {datos[2]}\nCantidad Disponible: {datos[3]}" # regresamos el nombre y precio del producto
            
    if encontrado == 0:
        return "Producto no encontrado"
            

# Funcion de busqueda por rango de precios
def brango(rango_i:int, rango_f:int):
    lista = []
    # rango_i seria precio inicial y rango_f seria precio final, para marcar el rango de los precios
    with open(inventario_path) as inventario:
        with open(results_path, 'w') as result:
            for linea in inventario: # por cada linea que hay en producto.txt
                datos = linea.split(",") # dividimos los datos de cada linea
                if int(datos[2]) >= rango_i and int(datos[2]) <= rango_f: # si los datos del precio es igual o mayor al rango inicial y menior o igual al rango final
                    result.write(f"{datos[0]}: ${datos[2]}\n")
                    print(f"{datos[0]}: ${datos[2]}") # agregamos el nombre del producto y su precio dentro del arreglo llamado lista
                    lista.append(datos[0])
                
    print("\nHay un total de", len(lista), "productos con ese rango de precio")


# Funcion para retornar el stock disponible
def bstock(producto):
    # vamos a abrir el archivo plano donde estan almacenados los productos
    with open(inventario_path) as inventario:
        for linea in inventario: # por cada linea que tiene el archivo plano
            datos = linea.split(",") # dividiremos los datos que tiene cada linea
            if producto in datos[0] or producto in datos[1]: # si el nombre del producto o codigo esta dentro de la linea
                return int(datos[3]) # retornamos cuanto tenemos en stock


# Funcion para retornar precio de un producto
def bprecio(producto):
    # vamos a abrir el archivo plano donde estan almacenados los productos
    with open(inventario_path) as inventario:
        for linea in inventario: # por cada linea que tiene el archivo plano
            datos = linea.split(",") # dividiremos los datos que tiene cada linea
            if producto in datos[0] or producto in datos[1]: # si el nombre del producto o codigo esta dentro de la linea
                return int(datos[2]) # retornamos cuanto cuesta el producto


# Funcion para hacer una busqueda por medio de codigo o nombre de producto
def bproducto(producto):
    encontrado = 0
    # vamos a abrir el archivo plano donde estan almacenados los productos
    with open(inventario_path) as inventario:
        for linea in inventario: # por cada linea que tiene el archivo plano
            datos = linea.split(",") # vamos a dividir los datos de cada linea dentro de un arreglo

            if producto == datos[1] or producto == datos[0]: # si el codigo del producto esta dentro de la linea
                encontrado = 1
                return datos[0]
            
    if encontrado == 0:
        # return "Producto no encontrado"
        return False


# Funcion para mostrar todos los productos disponibles
def mostrarProductos():
    with open(inventario_path) as inventario:
        for linea in inventario:
            producto = linea.split(",")
            print(producto[0])


# Muestra los articulos agotados, los que tienen stock 0
def agotados():
    system('cls')
    print("Productos agotados: ")
    with open(inventario_path) as inventario:
        for linea in inventario:
            producto = linea.split(",")
            if producto[3] == "0\n":
                print(producto[0])
    

# Muestra los articulos disponibles, stock mayor a 0
def disponibles():
    system('cls')
    print("Productos disponibles: ")
    with open(inventario_path) as products_file:
        for linea in products_file:
            producto = linea.split(",")
            if producto[3] != "0\n":
                print(producto[0])
    
    input("\nPresiona Enter para seguir")
