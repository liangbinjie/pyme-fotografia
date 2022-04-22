from buscador import agotados, disponibles


ventas_path = 'reportes/ventas.txt'
compras_path = 'reportes/compras.txt'

# Funcion para buscar dentro de las ventas (subtotales)
def verVentas():
    ventas = [] # arreglo que se utilizara
    with open(ventas_path) as ventas_file: # abrimos el archivo donde se contiene las ventas
        for venta in ventas_file: # por cada linea/venta que hay en el archivo
            ventas.append(int(venta)) # las agregamos al arreglo de ventas
            
    ventaMayor = 0 # variable para buscar la venta mayor
    for venta in ventas:
        if venta >= ventaMayor:
            ventaMayor = venta

# Buscamos el indice de la venta mayor
    for venta in range(len(ventas)):
        if ventaMayor == ventas[venta]:
            indice = venta
    
    return ventas, ventaMayor, indice


# Funcion para buscar la compra utilizando el indice de la venta mas alta
def buscar_compra(indice):
    with open(compras_path, 'r') as compras_file:
        compra = compras_file.readlines()
    
    return "Detalles de la compra: " + compra[indice]


def verReporte():
    # Funcion para ver un reporte general, donde se puede mostrar
        # Venta mas alta
        # Monto total de las ventas
        # Promedio de ventas
    ventas, ventaMayor, indice  = verVentas()
    sumaTotal = 0

    for venta in ventas:
        sumaTotal += venta

    print(f"Suma total del dia: ${sumaTotal}\n")
    print(f"Venta mas alta: ${ventaMayor}")
    print(buscar_compra(indice))
    promedio = sumaTotal/len(ventas)
    print(f"Promedio de ventas: ${promedio}")
    input("\nPresiona Enter para seguir")
    disponibles()
    agotados()


"""
def crearReporteDiario():
    fecha = input("Vuelva el (dia-mes-año) de hoy: ")
    with open(f'reportes/reporte {fecha}.txt', 'a') as reporte_dia:
        reporte_dia.write(f"Reportes del dia {fecha}\n")

    return fecha


def cerrarReporteDiario(fecha):
    f = open(ventas_path, 'r')
    data = f.read()
    
    nf = open(f'reportes/reporte {fecha}.txt', 'a')
    nf.write(data)


def generarReporte():
    fecha = input("Digite (dia-mes-año) para generar reporte: ")
    # Venta mas alta
    # Ventas
    # Cuanto se vendio
    # Promedio de ventas
    # Promedio de ventas por producto
    with open(f'reportes/reporte {fecha}.txt', 'r') as reporte_dia:
        reporte = reporte_dia.read()
        print(reporte)
"""