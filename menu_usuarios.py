from gestion_datos import cargar_datos_usuarios, guardar_datos_usuarios
from gestion_usuarios import (agregar_usuario, listar_usuarios, buscar_usuario, actualizar_usuario, eliminar_usuario)

def menu():
    datos = cargar_datos_usuarios()

    while True:
        AZUL = "\033[34m"
        VERDE = "\033[32m"
        RESET = "\033[0m"

        print(f"""
{AZUL}=====================================
      Menú de Gestión de Usuarios
====================================={RESET}

{VERDE}1. Crear Usuario{RESET}
{VERDE}2. Listar Usuarios{RESET}
{VERDE}3. Buscar Usuario{RESET}
{VERDE}4. Actualizar Usuario{RESET}
{VERDE}5. Eliminar Usuario{RESET}
{VERDE}6. Guardar y Salir{RESET}

{AZUL}====================================={RESET}
        """)

        opcion = input("Seleccione una opción: ")

        # ---------------- CREAR USUARIO ----------------
        if opcion == "1":
            id_usuario = input("Ingrese el ID del Usuario (4 ultimos dígitos de su cedula): ")

            if id_usuario in datos["usuarios"]:
                print("El usuario ya existe.")
                input("Presione Enter para continuar...")
                continue

            nombre = input("Ingrese Nombre: ")
            apellido = input("Ingrese Apellido: ")
            telefono = input("Ingrese Teléfono: ")
            direccion = input("Ingrese Dirección: ")
            tipo = input("Ingrese tipo de Usuario (usuario/administrador): ")

            agregar_usuario(datos, id_usuario, nombre, apellido, telefono, direccion, tipo)

        # ---------------- LISTAR ----------------
        elif opcion == "2":
            listar_usuarios(datos)

        # ---------------- BUSCAR ----------------
        elif opcion == "3":
            id_usuario = input("Ingrese el ID del Usuario a buscar: ")
            buscar_usuario(datos, id_usuario)

        # ---------------- ACTUALIZAR ----------------
        elif opcion == "4":
            id_usuario = input("Ingrese el ID del Usuario a actualizar: ")
            nombre = input("Ingrese Nombre: ")
            apellido = input("Ingrese Apellido: ")
            telefono = input("Ingrese Teléfono: ")
            direccion = input("Ingrese Dirección: ")
            tipo = input("Ingrese tipo de Usuario: ")

            actualizar_usuario(datos, id_usuario, nombre, apellido, telefono, direccion, tipo)

        # ---------------- ELIMINAR ----------------
        elif opcion == "5":
            id_usuario = input("Ingrese el ID del Usuario a eliminar: ")
            eliminar_usuario(datos, id_usuario)

        # ---------------- GUARDAR Y SALIR ----------------
        elif opcion == "6":
            guardar_datos_usuarios(datos)
            print("\nDatos guardados correctamente. Saliendo...\n")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

        input("Presione Enter para continuar...")


# Esto evita que se ejecute automáticamente cuando lo importemos en main.py
if __name__ == "__main__":
    menu()
