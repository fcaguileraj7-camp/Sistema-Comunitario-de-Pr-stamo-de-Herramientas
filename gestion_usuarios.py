from gestion_logs import registrar_log

def agregar_usuario (datos, id_usuario, nombre, apellido, telefono, direccion, tipo_usuario):

    if id_usuario in datos["usuarios"]:
        print(f"El usuario con ID {id_usuario} ya existe.")
        registrar_log(f"Intento de crear usuario duplicado: {id_usuario}")
        return
    
    datos["usuarios"][id_usuario] = {
    "nombre": nombre,
    "apellido": apellido,
    "telefono": telefono,
    "direccion": direccion,
    "tipo_usuario": tipo_usuario,
    "activo": True
}

    print(f"\n\nUsuario {nombre} agregado exitosamente.\n\n")

def listar_usuarios(datos):

    if not datos["usuarios"]:
        print("No hay usuarios registrados.")
        return
    
    print("\n\nLista de usuarios:\n")
    for id_usuario, info in datos["usuarios"].items():
         if not info.get("activo", True):
            continue
         
    print(f"ID: {id_usuario}")
    print(f"Nombre: {info['nombre']}")
    print(f"Apellido: {info['apellido']}")
    print(f"Teléfono: {info['telefono']}")
    print(f"Dirección: {info['direccion']}")
    print(f"Tipo de usuario: {info['tipo_usuario']}\n")

def buscar_usuario(datos, id_usuario):

    if id_usuario in datos["usuarios"]:
        info = datos["usuarios"][id_usuario]
        print(f"\n\nInformación del usuario con ID {id_usuario}:")
        print(f"Nombre: {info['nombre']}")
        print(f"Apellido: {info['apellido']}")
        print(f"Teléfono: {info['telefono']}")
        print(f"Dirección: {info['direccion']}")
        print(f"Tipo de usuario: {info['tipo_usuario']}\n")
    else:
        print(f"\n\nUsuario con ID {id_usuario} no encontrado.\n\n")

def actualizar_usuario(datos, id_usuario, nombre, apellido, telefono, direccion, tipo_usuario):

    if id_usuario in datos["usuarios"]:
        datos["usuarios"][id_usuario] = {
            "nombre": nombre,
            "apellido": apellido,
            "telefono": telefono,
            "direccion": direccion,
            "tipo_usuario": tipo_usuario
        }
        print(f"\n\nUsuario con ID {id_usuario} actualizado exitosamente.\n\n")
    else:
        print(f"\n\nUsuario con ID {id_usuario} no encontrado.\n\n")
        

def eliminar_usuario(datos, id_usuario):

    if id_usuario in datos["usuarios"]:

        if not datos["usuarios"][id_usuario]["activo"]:
            print("El usuario ya está inactivo.")
            return

        datos["usuarios"][id_usuario]["activo"] = False
        print(f"\nUsuario con ID {id_usuario} inactivado correctamente.\n")

    else:
        print(f"\nUsuario con ID {id_usuario} no encontrado.\n")


