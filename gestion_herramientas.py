from gestion_logs import registrar_log

def agregar_herramienta(datos, id_herramienta, nombre, categoria, cantidad_disponible, estado, valor_estimado):

    if id_herramienta in datos["herramientas"]:
        print(f"La herramienta con ID {id_herramienta} ya existe.")
        registrar_log(f"Intento de crear herramienta duplicada: {id_herramienta}")
        return

    datos["herramientas"][id_herramienta] = {
        "nombre": nombre,
        "categoria": categoria,
        "cantidad_disponible": cantidad_disponible,
        "estado": estado,
        "valor_estimado": valor_estimado,
        "activo": True
    }
    print(f"\nHerramienta {nombre} agregada exitosamente.\n")


def listar_herramientas(datos):

    if not datos["herramientas"]:
        print("No hay herramientas registradas.")
        return

    print("\nLista de Herramientas:\n")

    for id_herramienta, info in datos["herramientas"].items():
        if not info["activo"]:
            continue

        print(f"ID: {id_herramienta}")
        print(f"Nombre: {info['nombre']}")
        print(f"Categoría: {info['categoria']}")
        print(f"Cantidad Disponible: {info['cantidad_disponible']}")
        print(f"Estado: {info['estado']}")
        print(f"Valor Estimado: {info['valor_estimado']}\n")


def buscar_herramienta(datos, id_herramienta):

    if id_herramienta in datos["herramientas"]:
        info = datos["herramientas"][id_herramienta]

        print(f"\nInformación de la herramienta {id_herramienta}:")
        print(f"Nombre: {info['nombre']}")
        print(f"Categoría: {info['categoria']}")
        print(f"Cantidad Disponible: {info['cantidad_disponible']}")
        print(f"Estado: {info['estado']}")
        print(f"Valor Estimado: {info['valor_estimado']}\n")
    else:
        print("Herramienta no encontrada.")


def actualizar_herramientas(datos, id_herramienta, nombre, categoria, cantidad_disponible, estado, valor_estimado):

    if id_herramienta in datos["herramientas"]:
        datos["herramientas"][id_herramienta] = {
            "nombre": nombre,
            "categoria": categoria,
            "cantidad_disponible": cantidad_disponible,
            "estado": estado,
            "valor_estimado": valor_estimado
        }

        print("Herramienta actualizada correctamente.")
    else:
        print("Herramienta no encontrada.")


def cambiar_estado_herramienta(datos, id_herramienta, nuevo_estado):

    if id_herramienta in datos["herramientas"]:
        datos["herramientas"][id_herramienta]["estado"] = nuevo_estado
        print("Estado actualizado correctamente.")
    else:
        print("Herramienta no encontrada.")


def inactivar_herramienta(datos, id_herramienta):

    if id_herramienta in datos["herramientas"]:

        if not datos["herramientas"][id_herramienta]["activo"]:
            print("La herramienta ya está inactiva.")
            return

        datos["herramientas"][id_herramienta]["activo"] = False
        print("Herramienta inactivada correctamente.")

    else:
        print("Herramienta no encontrada.")
