from buscador import *
from modificador import *
from os import system

enter = "Presiona Enter para seguir"

def inventario():
    running = True

    while running:
        print("Que desea hacer?\n[1]Buscar\n[2]Agregar\n[3]Eliminar\n[4]Modificar\n[0]Salir")
        do = input("> ").lower()

        if do == "buscar" or do == "1":
            system("cls")
            print('- - - - - - - - - - - - - - - - - - - -')
            tipo = input("Tipo de busqueda\n[1]General\n[2]Precio\n\n > ").lower()
            print('- - - - - - - - - - - - - - - - - - - -')

            if tipo == "general" or tipo == "1":
                nombre_producto = input("Ingrese nombre de producto o codigo: ").lower()
                print(bgeneral(nombre_producto))
                txt(bgeneral(nombre_producto))
            
                input(enter)
                system("cls")


            elif tipo == "precio" or tipo == "2":
                system("cls")
                rango_i = int(input("Ingrese precio inicial: "))
                rango_f = int(input("Ingrese precio de rango final: "))
                print("- "*13+"\n")
                if rango_f < rango_i:
                    print("\nPrecio de rango final invalido\nIntente denuevo")

                else:
                    brango(rango_i, rango_f)
                
                input(enter)
                system("cls")



        elif do == "agregar" or do == "2":
            system("cls")
            print('- - - - - - - - - - - - - - - - - - - -')
            nombre_producto = input("Nombre de producto a agregar: ").lower()
            codigo = input("Ingrese codigo de producto: ")
            precio = input("Ingrese precio de producto: ")
            stock = input("Ingrese cantidad de productos en inventario: ")
            
            if "" in (nombre_producto,codigo,precio,stock):
                system('cls')
                print("No se puedo agregar el producto, requiere informacion")
            
            else:
                agregar(nombre_producto, codigo, precio, stock)
            input(enter)
            system("cls")
        
        elif do == "modificar" or do == "4":
            system("cls")
            print('- - - - - - - - - - - - - - - - - - - -')
            producto = input("Nombre o codigo del producto: ")
            producto = bproducto(producto)
            if producto != False:
                dato = input("Tipo de dato: ")
                nuevo = input("Dato nuevo: ")
                modificar(producto, dato, nuevo)
                print("Articulo modificado")
            
            else:
                print("Producto no encontrado")
                
            input(enter)
            system("cls")




        elif do == "eliminar" or do == "3":
            system("cls")
            print('- - - - - - - - - - - - - - - - - - - -')
            producto = input("Ingrese nombre o codigo de producto: ")
            eliminar(producto)

            input(enter)
            system("cls")




        # print('- - - - - - - - - - - - - - - - - - - -')

        if do.lower() == "salir" or do == "0":
            running = False