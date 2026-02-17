from gestion_datos import (cargar_datos_prestamos, guardar_datos_prestamos, cargar_datos_usuarios, cargar_datos_herramientas, guardar_datos_herramientas)
from gestion_prestamos import (listar_solicitudes_pendientes, aprobar_prestamo, rechazar_prestamo, devolver_prestamo, herramientas_stock_bajo, prestamos_activos, prestamos_vencidos, historial_usuario, herramientas_mas_solicitadas, usuarios_mas_activos)

def menu():
    datos_prestamos = cargar_datos_prestamos()
    datos_usuarios = cargar_datos_usuarios()
    datos_herramientas = cargar_datos_herramientas()

    while True:
        AZUL = "\033[34m"
        VERDE = "\033[32m"
        RESET = "\033[0m"
        
        print(f"""
{AZUL}=====================================
      Menú de Gestión de Préstamos
====================================={RESET}

{VERDE}1. Ver solicitudes pendientes{RESET}
{VERDE}2. Aprobar solicitud{RESET}
{VERDE}3. Rechazar solicitud{RESET}
{VERDE}4. Registrar devolución{RESET}
{VERDE}5. Consultas y Reportes{RESET}
{VERDE}6. Guardar y salir{RESET}

{AZUL}====================================={RESET}
        """)
        
        opcion = input("Seleccione una opción:  ")

        if opcion == "1":
            listar_solicitudes_pendientes(datos_prestamos)
            input("Presione Enter para continuar...")

        elif opcion == "2":
            id_prestamo = input("Ingrese ID de la solicitud a aprobar: ")
            aprobar_prestamo(datos_prestamos, datos_herramientas, id_prestamo)
            input("Presione Enter para continuar...")

        elif opcion == "3":
            id_prestamo = input("Ingrese ID de la solicitud a rechazar: ")
            rechazar_prestamo(datos_prestamos, id_prestamo)
            input("Presione Enter para continuar...")

        elif opcion == "4":
            id_prestamo = input("Ingrese ID del préstamo a devolver: ")
            devolver_prestamo(datos_prestamos, datos_herramientas, id_prestamo)
            input("Presione Enter para continuar...")

        elif opcion == "5":        

            while True:
                print(f"""
                      
{AZUL}=====================================
      Menú Consultas y Reportes
====================================={RESET}

{VERDE}1. Herramientas con stock bajo{RESET}
{VERDE}2. Préstamos activos{RESET}
{VERDE}3. Préstamos vencidos{RESET}
{VERDE}4. Historial por usuario{RESET}
{VERDE}5. Herramientas más solicitadas{RESET}
{VERDE}6. Usuarios más activos{RESET}
{VERDE}7. Volver{RESET}

{AZUL}====================================={RESET}
        """)

                subopcion = input("Seleccione una opción: ")

                if subopcion == "1":
                    herramientas_stock_bajo(datos_herramientas)
                    input("Presione Enter para continuar...")

                elif subopcion == "2":
                    prestamos_activos(datos_prestamos)
                    input("Presione Enter para continuar...")
                
                elif subopcion == "3":
                    prestamos_vencidos(datos_prestamos)
                    input("Presione Enter para continuar...")

                elif subopcion == "4":
                    usuario_id = input("Ingrese ID del usuario: ")
                    historial_usuario(datos_prestamos, usuario_id)
                    input("Presione Enter para continuar...")

                elif subopcion == "5":
                    herramientas_mas_solicitadas(datos_prestamos)
                    input("Presione Enter para continuar...")

                elif subopcion == "6":
                    usuarios_mas_activos(datos_prestamos)
                    input("Presione Enter para continuar...")

                elif subopcion == "7":
                    break

                else:

                    print("Opción inválida.")

                    input("Presione Enter para continuar...")
                    
        elif opcion == "6":

            guardar_datos_prestamos(datos_prestamos)
            guardar_datos_herramientas(datos_herramientas)

            print("Datos guardados correctamente.")
            break

        else:
            print("Opción inválida.")
            input("Presione Enter para continuar...")


if __name__ == "__main__":
    menu()
        