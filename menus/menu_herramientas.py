from gestion_datos import cargar_datos, guardar_datos
from gestion_herramientas import agregar_herramienta, listar_herramienta, buscar_herramienta, actualizar_herramientas, eliminar_herramienta

def menu():
    datos = cargar_datos()

    while True:
        AZUL = "\033[34m"
        VERDE = "\033[32m"
        RESET = "\033[0m"
        
        print(f"""
{AZUL}=====================================
      Menú de Gestión de Herramientas
====================================={RESET}

{VERDE}1. Agregar Herramienta{RESET}
{VERDE}2. Listar Herramientas{RESET}
{VERDE}3. Buscar Herramienta{RESET}
{VERDE}4. Actualizar Herrramienta{RESET}
{VERDE}5. Eliminar Herramienta{RESET}
{VERDE}6. Guardar y salir{RESET}

{AZUL}====================================={RESET}
        """)
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_herramienta = input("\n\n\nIngrese el ID de la Herramienta:  ")
            agregar_herramienta(datos, id_herramienta)
        elif opcion == "2":
            listar_herramienta(datos)
        elif opcion == "3":
            buscar_herramienta(datos, id_herramienta)
            pass
           
        elif opcion == "4":
            id_herramienta = input("\n\n\nIngrese el ID de la Herramienta:   ")
            categoria = 

        elif opcion == "5":
            pass
        elif opcion == "6":
            guardar_datos(datos)
            print("Datos guardados. Saliendo ... \n\n")
            break
        else:
            print("Opción inválida. Intente de nuevo")
        input("Presione cualquier tecla para continuar ....")


menu(

)
        