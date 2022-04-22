"""
Modulo donde se implementan funciones que modifican el inventario
Funciones como agregar productos
Eliminar productos
Cambiar informacion del producto
"""

import os
from buscador import *

inventario_path = "txt/inventario.txt"
eliminado_path = "txt/eliminados.txt"
modificado_path = "txt/modificado.txt"

def agregar(nombre_producto, codigo, precio, stock):
    with open(inventario_path, 'a') as inventario:
        inventario.write(f"{nombre_producto},{codigo},{precio},{stock}\n")
    
    print("Producto:", nombre_producto, "| añadido a la base de datos")


def eliminar(producto):
    encontrado = 0
    with open(inventario_path, 'r') as inventario:
        with open(eliminado_path, 'w') as eliminado_file:
            for linea in inventario:
                datos = linea.split(",")

                if producto not in datos:
                    eliminado_file.write(linea)
                
 
                if producto in datos:
                    encontrado = 1
                    print("Eliminando producto:", datos[0], "\nCodigo:", datos[1])


    os.replace(eliminado_path, inventario_path)
    
    if encontrado == 0:
        print("Producto no encontrado")
    
    else:
        print("\nProducto eliminado")
                    

def modificar(producto, dato, nuevo):
    # Primero buscamos el producto
    with open(inventario_path, 'r') as inventario:
        with open(modificado_path, 'w') as modificado:
            for line in inventario:
                datos = line.split(",")

                if producto not in datos:
                        modificado.write(line)

                if producto in datos:

                    if dato == "nombre":
                        modificado.write(f"{nuevo},{datos[1]},{datos[2]},{datos[3]}")
                    
                    if dato == "codigo":
                        modificado.write(f"{datos[0]},{nuevo},{datos[2]},{datos[3]}")

                    if dato == "precio":
                        modificado.write(f"{datos[0]},{datos[1]},{nuevo},{datos[3]}")

                    if dato == "stock":
                        modificado.write(f"{datos[0]},{datos[1]},{datos[2]},{nuevo}\n")

    os.replace(modificado_path, inventario_path)

