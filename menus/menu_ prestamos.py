from gestion_datos import cargar_datos, guardar_datos
from gestion_prestamos import registrar_prestamo, eliminar_prestamo, consultas_reportes

def menu():
    datos = cargar_datos()

    while True:
        AZUL = "\033[34m"
        VERDE = "\033[32m"
        RESET = "\033[0m"
        
        print(f"""
{AZUL}=====================================
      Menú de Gestión de Usuarios
====================================={RESET}

{VERDE}1. Registrar Prestamo Herramienta{RESET}
{VERDE}2. Registrar Retorno Herramienta{RESET}
{VERDE}3. Consultas y Reportes{RESET}
{VERDE}4. Guardar y salir{RESET}

{AZUL}====================================={RESET}
        """)
        
        opcion = input("Seleccione una opción:  ")

        if opcion == "1":
            id_prestamo = input("\n\n\nIngrese el ID de el usuario (los 4 ultimos digitos de su cedula):  ")
            registrar_prestamo(datos, id_prestamo)

        elif opcion == "2":
            id_usuario = input("Ingrese ID de Usuario (los 4 ultimos digitos de su cedula): ")
            eliminar_prestamo(datos, id_prestamo)

        elif opcion == "3":
            id_herramienta = input("Ingrese el ID de la Herramienta:  ")
            consultas_reportes(datos, id_herramienta)

        elif opcion == "4":
            guardar_datos(datos)
            print("Datos guardados. Saliendo ... \n\n")
            break
        else:
            print("Opción inválida. Intente de nuevo")
        input("Presione cualquier tecla para continuar ....")


menu(

)
        