from gestion_datos import cargar_datos_herramientas, guardar_datos_herramientas
from gestion_herramientas import agregar_herramienta, listar_herramientas, buscar_herramienta, actualizar_herramientas, cambiar_estado_herramienta

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
{VERDE}5. Cambiar Estado Herramienta{RESET}
{VERDE}6. Guardar y salir{RESET}

{AZUL}====================================={RESET}
        """)
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_herramienta = input("Ingrese ID: ")

            if id_herramienta in datos["herramientas"]:
                print("La herramienta ya existe.")
                input("Presione Enter para continuar...")
                continue

            nombre = input("Ingrese Nombre: ")
            categoria = input("Ingrese Categoría (Construcción / Jardinería): ")
            cantidad = int(input("Ingrese Cantidad Disponible: "))
            estado = input("Ingrese Estado (activa/en reparación/fuera de servicio): ")
            valor = int(input("Ingrese Valor Estimado: "))

            agregar_herramienta(datos, id_herramienta, nombre, categoria, cantidad, estado, valor)

        elif opcion == "2":
            listar_herramientas(datos)

        elif opcion == "3":
            id_herramienta = input("Ingrese ID a buscar: ")
            buscar_herramienta(datos, id_herramienta)
            
        elif opcion == "4":
            id_herramienta = input("Ingrese ID a actualizar: ")
            nombre = input("Ingrese Nombre: ")
            categoria = input("Ingrese Categoría: ")
            cantidad = int(input("Ingrese Cantidad Disponible: "))
            estado = input("Ingrese Estado: ")
            valor = int(input("Ingrese Valor Estimado: "))

            actualizar_herramientas(datos, id_herramienta, nombre, categoria, cantidad, estado, valor)

        elif opcion == "5":
            id_herramienta = input("Ingrese ID: ")

            print("\nSeleccione nuevo estado:")
            print("1. Activa")
            print("2. En reparación")
            print("3. Fuera de servicio")

            estado_opcion = input("Opción: ")

            if estado_opcion == "1":
                nuevo_estado = "activa"
            elif estado_opcion == "2":
                nuevo_estado = "en reparación"
            elif estado_opcion == "3":
                nuevo_estado = "fuera de servicio"
            else:
                print("Opción inválida.")
                continue

            cambiar_estado_herramienta(datos, id_herramienta, nuevo_estado)


        elif opcion == "6":
            guardar_datos_herramientas(datos)
            print("Datos guardados correctamente.")
            break

        else:
            print("Opción inválida.")

        input("Presione Enter para continuar...")


if __name__ == "__main__":
    menu()
        