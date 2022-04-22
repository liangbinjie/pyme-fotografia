from inventario import inventario
from comprar import *
from os import system
from getpass import getpass
from reclamos import *
from reportes import verReporte


enter = "\nPresiona Enter para seguir"

def admin():
    basedatos = {"admin": "admin1234", "benji": "1386"}
    intentos = 1

    usuario = input("Usuario: ")
    contra = getpass("Contraseña: ")


    while usuario not in basedatos or contra != basedatos[usuario]:
        intentos += 1
        print("Invalido, intente otra vez")
        usuario = input("Usuario: ")
        contra = getpass("Contraseña: ")
        if intentos == 3:
            print("Has usado el numero maximo de intentos")
            quit()


    else:
        running = True
        while running:
            system("cls")
            print("Adonde quieres entrar?\n[1]Inventario\n[2]Reportes\n[3]Ver Reclamos\n[4]Salir")
            admin = input("> ")

            if admin == "1":
                system("cls")
                print("Has entrado al inventario")
                inventario()
                system('cls')


            if admin == "2":
                system("cls")
                verReporte()
                input(enter)
                system('cls')

            if admin == "3":
                verReclamos()
                input(enter)
                system('cls')

            if admin == "4":
                system('cls')
                break