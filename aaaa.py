def registrar_pedido(pedidos):
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    ID_libro = input("Ingrese la ID del libro: ")
    fecha = input("Ingrese la fecha del prestamo: ")
    devolucion = input("Ingrese la fecha de devolucion: ")
    pedido = {
        'nombre': nombre,
        'apellido': apellido,
        'ID de libro': ID_libro,
        'fecha de prestamo': fecha,
        'fecha de devolucion': devolucion,
    }
    
    pedidos.append(pedido)
    print("Pedido registrado exitosamente.")

def listar_pedidos(pedidos):
    if not pedidos:
        print("No hay pedidos registrados.")
        return

    for pedido in pedidos:
        print(f"Cliente: {pedido['nombre']} {pedido['apellido']}")
        print(f"ID de libro: {pedido['ID de libro']}")
        print(f"fecha de prestamo: {pedido['fecha de prestamo']}")
        print(f"fecha de devolucion: {pedido['fecha de devolucion']}")
        print("")

def imprimir_hoja_de_ruta(pedidos):
    if not pedidos:
        print("No hay pedidos registrados.")
        return
    
    ID_libro = input("Ingrese la ID del libro para generar la hoja de ruta: ")
    pedidos_ID_libro = [pedido for pedido in pedidos if pedido['ID de libro'] == ID_libro]
    
    if not pedidos_ID_libro:
        print(f"No hay pedidos registrados para el ID del libro {ID_libro}.")
        return

    with open(f"hoja_de_ruta_{ID_libro}.txt", "w") as file:
        for pedido in pedidos_ID_libro:
            file.write(f"Cliente: {pedido['nombre']} {pedido['apellido']}\n")
            file.write(f"ID de libro: {pedido['ID de libro']}\n")
            file.write(f"fecha de prestamo: {pedido['fecha de prestamo']}\n")
            file.write(f"fecha de devolucion: {pedido['fecha de devolucion']}\n")
            file.write("\n")
    
    print(f"Hoja de ruta para el ID de libro {ID_libro} generada exitosamente.")

def salir():
    print("Saliendo del programa. ¡Hasta luego!")
