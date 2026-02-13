from gestion_datos import cargar_datos_herramientas, guardar_datos_herramientas
from gestion_herramientas import agregar_herramienta, listar_herramienta, buscar_herramienta, actualizar_herramientas, eliminar_herramienta, activar_inactivar

def menu():
    datos = cargar_datos_herramientas()

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
{VERDE}5. Activar o Inactivar Herramienta{RESET}
{VERDE}6. Eliminar Herramienta{RESET}
{VERDE}7. Guardar y salir{RESET}

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
            categoria = input("Igrese categoria:  ")
            cantidad = input("Ingrese cantidad: ")
            disponibilidad = input("Ingrese disponibilidad:  ")
            actualizar_herramientas(datos, id_herramienta, categoria, cantidad, disponibilidad)

        elif opcion == "5":
            id_herramienta = input("\n\n\nIngrese ID de la herramienta: ")
            activar_inactivar(datos, id_herramienta)

        elif opcion == "6":
            id_herramienta = input("\n\n\nIngrese ID de la herramienta: ")
            eliminar_herramienta(datos, id_herramienta)

        elif opcion == "7":
            guardar_datos_herramientas(datos)
            print("Datos guardados. Saliendo ... \n\n")
            break
        else:
            print("Opción inválida. Intente de nuevo")
        input("Presione cualquier tecla para continuar ....")


menu(

)
        