from reclamos import *
from comprar import *
from os import system

enter = "\nPresiona Enter para seguir"

def cliente(respuesta):

    running = True

    while running:
        if respuesta == "1":
            print("Que quieres realizar?\n[1]Compra\n[2]Ver Productos\n[3]Reclamar\n[4]Salir")
            client = input("> ")
            system('cls')
            if client == "1":
                system('cls')
                proceso_compra()
                
            if client == "2":
                system('cls')
                mostrarProductos()
                input(enter)
                system('cls')
            
            if client == "3":
                system('cls')
                agregar_reclamo()
                input(enter)
                system('cls')

            if client == "4":
                system('cls')
                break

