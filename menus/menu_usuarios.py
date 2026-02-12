from gestion_datos import cargar_datos, guardar_datos
from gestion_usuarios import agregar_usuario, listar_usuarios, buscar_usuario, actualizar_usuario, eliminar_usuario

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

{VERDE}1. Crear Usuario{RESET}
{VERDE}2. Listar Usuarios{RESET}
{VERDE}3. Buscar Usuario{RESET}
{VERDE}4. Actualizar Usuario{RESET}
{VERDE}5. Eliminar Usuario{RESET}
{VERDE}6. Guardar y salir{RESET}

{AZUL}====================================={RESET}
        """)
        
        opcion = input("Seleccione una opción:  ")

        if opcion == "1":
            id_usuario = input("\n\n\nIngrese el ID de la usuario (los 4 ultimos digitos de su cedula):  ")
            agregar_usuario(datos, id_usuario)

        elif opcion == "2":
            listar_usuarios(datos)

        elif opcion == "3":
            buscar_usuario(datos, id_usuario)
            pass
        elif opcion == "4":
            id_usuario = input("\n\n\nIngrese el ID del Usuario (los 4 ultimos digitos de su cedula):  ")
            nombre = input("Ingrese Nombre: ")
            apellido = input(" Ingrese Apellido: ")
            telefono = input("Ingrese Telefono: ")
            direccion = input("Ingrese Dirección: ")
            tipo = input("Ingrese tipo de Usuario: ")
            
            actualizar_usuario(datos, id_usuario, nombre, apellido, telefono, direccion, tipo)

        elif opcion == "5":
            id_usuario = input("\n\n\nIngrese ID del Usuario (los 4 ultimos digitos de su cedula):  ")
            eliminar_usuario(datos, id_usuario)

        elif opcion == "6":
            guardar_datos(datos)
            print("Datos guardados. Saliendo ... \n\n")
            break
        else:
            print("Opción inválida. Intente de nuevo")
        input("Presione cualquier tecla para continuar ....")


menu(

)
        