# Importar las funciones desde el archivo de funciones
from aaaa import registrar_pedido, listar_pedidos, imprimir_hoja_de_ruta, salir

# Lista para almacenar los pedidos
pedidos = []

# Programa principal
while True:
    print("\nSistema de Gestión de Pedidos - Gaxplosive")
    print("1. Registrar pedido")
    print("2. Listar todos los pedidos")
    print("3. Imprimir hoja de ruta")
    print("4. Mostrar hoja de ruta")
    print("5. Salir del programa")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        registrar_pedido(pedidos)
    elif opcion == '2':
        listar_pedidos(pedidos)
    elif opcion == '3':
        imprimir_hoja_de_ruta(pedidos)
    elif opcion == '4':
        mostrar_hoja_de_ruta()
    elif opcion == '5':
        salir()
        break
    else:
        print("Opción no válida. Intente de nuevo.")

def mostrar_hoja_de_ruta():
    ID_libro = input("Ingrese el ID del libro para mostrar la hoja de ruta: ")
    try:
        with open(f"hoja_de_ruta_{ID_libro}.txt", "r") as file:
            print(f"Contenido de la hoja de ruta para el ID de libro {ID_libro}:")
            print(file.read())
    except FileNotFoundError:
        print(f"No existe hoja de ruta para el ID de libro {ID_libro}.")
    except Exception as e:
        print(f"Error al abrir el archivo: {e}")
