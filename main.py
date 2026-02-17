from menu_usuarios import menu as menu_usuarios
from menu_herramientas import menu as menu_herramientas
from menu_prestamos import menu as menu_prestamos
from gestion_datos import cargar_datos_herramientas, cargar_datos_prestamos, cargar_datos_usuarios, guardar_datos_prestamos
from gestion_prestamos import consultar_estado_herramienta, crear_solicitud

def main():

    while True:
        AZUL = "\033[34m"
        VERDE = "\033[32m"
        RESET = "\033[0m"
        print(f"""
{AZUL}====================================={RESET}
   SISTEMA COMUNITARIO DE HERRAMIENTAS
{AZUL}====================================={RESET}

{VERDE}1. Ingresar como Administrador{RESET}
{VERDE}2. Ingresar como Usuario{RESET}
{VERDE}3. Salir{RESET}

{AZUL}====================================={RESET}
        """)

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            password = input("Ingrese la contraseña de administrador: ")
            if password == "123456":
                menu_administrador()
            else:
             print("Contraseña incorrecta.")
             input("Presione Enter para continuar...")
            continue
        elif opcion == "2":
            menu_usuario()

        elif opcion == "3":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")

        input("Presione Enter para continuar...")

def menu_administrador():

    while True:
        AZUL = "\033[34m"
        VERDE = "\033[32m"
        RESET = "\033[0m"
        print(f"""
{AZUL}====================================={RESET}
        MENÚ ADMINISTRADOR
====================================={RESET}

{VERDE}1. Gestión de Usuarios.{RESET}
{VERDE}2. Gestión de Herramientas.{RESET}
{VERDE}3. Gestión de Préstamos.{RESET}
{VERDE}4. Volver al menú principal.{RESET}

{AZUL}====================================={RESET}
        """)

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_usuarios()

        elif opcion == "2":
            menu_herramientas()

        elif opcion == "3":
            menu_prestamos()

        elif opcion == "4":
            break

        else:
            print("Opción inválida.")

        input("Presione Enter para continuar...")


def menu_usuario():

    datos_herramientas = cargar_datos_herramientas()
    datos_prestamos = cargar_datos_prestamos()
    datos_usuarios = cargar_datos_usuarios()

    while True:
        AZUL = "\033[34m"
        VERDE = "\033[32m"
        RESET = "\033[0m"

        print(f"""
{AZUL}====================================={RESET}
            MENÚ USUARIO
{AZUL}====================================={RESET}

{VERDE}1. Consultar estado Herramienta{RESET}
{VERDE}2. Solicitar herramienta{RESET}
{VERDE}3. Volver al menú principal{RESET}

====================================={RESET}
        """)

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            herramienta_id = input("Ingrese el ID de la herramienta: ")
            consultar_estado_herramienta(
                datos_herramientas,
                datos_prestamos,
                herramienta_id
            )

        elif opcion == "2":

            id_prestamo = input("Ingrese ID de la solicitud: ")
            usuario_id = input("Ingrese su ID de usuario: ")
            herramienta_id = input("Ingrese ID de la herramienta: ")
            cantidad = int(input("Cantidad solicitada: "))
            fecha_inicio = input("Fecha inicio (YYYY-MM-DD): ")
            fecha_devolucion = input("Fecha estimada devolución (YYYY-MM-DD): ")
            observaciones = input("Observaciones: ")

            crear_solicitud(datos_prestamos, datos_usuarios, datos_herramientas, id_prestamo, usuario_id, herramienta_id, cantidad, fecha_inicio, fecha_devolucion, observaciones)

            guardar_datos_prestamos(datos_prestamos)

        elif opcion == "3":
            break

        else:
            print("Opción inválida.")

        input("Presione Enter para continuar...")


if __name__ == "__main__":
    main()
