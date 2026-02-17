from datetime import datetime
from gestion_logs import registrar_log

def crear_solicitud(datos_prestamos, datos_usuarios, datos_herramientas,
                    id_prestamo, usuario_id, herramienta_id,
                    cantidad, fecha_inicio, fecha_devolucion, observaciones):

    if id_prestamo in datos_prestamos["prestamos"]:
        print("La solicitud ya existe.")
        registrar_log(f"Intento de crear solicitud duplicada: {id_prestamo}")
        return

    if usuario_id not in datos_usuarios["usuarios"]:
        print("El usuario no existe.")
        registrar_log(f"Solicitud con usuario inexistente: {usuario_id}")
        return
    
    usuario = datos_usuarios["usuarios"][usuario_id]

    if not usuario.get("activo", True):
        print("El usuario está inactivo.")
        registrar_log(f"Solicitud con usuario inactivo: {usuario_id}")
        return

    if herramienta_id not in datos_herramientas["herramientas"]:
        print("La herramienta no existe.")
        registrar_log(f"Solicitud con herramienta inexistente: {herramienta_id}")
    
    herramienta = datos_herramientas["herramientas"][herramienta_id]

    if not herramienta.get("activo", True):
        print("La herramienta está inactiva.")
        registrar_log(f"Solicitud con herramienta inactiva: {herramienta_id}")
        return
    
    if cantidad <= 0:
        print("La cantidad debe ser mayor a cero.")
        return

    datos_prestamos["prestamos"][id_prestamo] = {
        "usuario_id": usuario_id,
        "herramienta_id": herramienta_id,
        "cantidad": cantidad,
        "fecha_inicio": fecha_inicio,
        "fecha_devolucion": fecha_devolucion,
        "estado": "pendiente",
        "observaciones": observaciones
    }

    print("Solicitud creada correctamente. Pendiente de aprobación.")
    registrar_log(f"Solicitud creada - ID: {id_prestamo}")


def aprobar_prestamo(datos_prestamos, datos_herramientas, id_prestamo):

    if id_prestamo not in datos_prestamos["prestamos"]:
        print("La solicitud no existe.")
        registrar_log(f"Aprobación fallida - no existe: {id_prestamo}")
        return

    prestamo = datos_prestamos["prestamos"][id_prestamo]

    if prestamo["estado"] != "pendiente":
        print("Este préstamo no está pendiente.")
        return

    herramienta_id = prestamo["herramienta_id"]
    cantidad = prestamo["cantidad"]

    herramienta = datos_herramientas["herramientas"][herramienta_id]

    if not herramienta.get("activo", True):
        print("La herramienta está inactiva.")
        return

    if herramienta["estado"] != "activa":
        print("Herramienta no disponible.")
        return
    
    if cantidad <= 0:
        print("Cantidad inválida.")
        return

    if herramienta["cantidad_disponible"] < cantidad:
        print("Stock insuficiente.")
        registrar_log(f"Aprobación fallida por stock - {id_prestamo}")
        return

    herramienta["cantidad_disponible"] -= cantidad
    prestamo["estado"] = "activo"

    print("Préstamo aprobado correctamente.")
    registrar_log(f"Préstamo aprobado - ID: {id_prestamo}")


def rechazar_prestamo(datos_prestamos, id_prestamo):

    if id_prestamo not in datos_prestamos["prestamos"]:
        print("La solicitud no existe.")
        return

    prestamo = datos_prestamos["prestamos"][id_prestamo]

    if prestamo["estado"] != "pendiente":
        print("Solo se pueden rechazar solicitudes pendientes.")
        return

    prestamo["estado"] = "rechazado"

    print("Solicitud rechazada.")
    registrar_log(f"Solicitud rechazada - ID: {id_prestamo}")


def listar_solicitudes_pendientes(datos_prestamos):

    print("\nSolicitudes Pendientes:\n")

    encontrada = False

    for id_prestamo, info in datos_prestamos["prestamos"].items():
        if info["estado"] == "pendiente":
            print(f"ID: {id_prestamo}")
            print(f"Usuario: {info['usuario_id']}")
            print(f"Herramienta: {info['herramienta_id']}")
            print(f"Cantidad: {info['cantidad']}")
            print(f"Fecha inicio: {info['fecha_inicio']}")
            print(f"Fecha devolución: {info['fecha_devolucion']}")
            print("---------------------------")
            encontrada = True

    if not encontrada:
        print("No hay solicitudes pendientes.")


def devolver_prestamo(datos_prestamos, datos_herramientas, id_prestamo):

    # Validar que exista el préstamo
    if id_prestamo not in datos_prestamos["prestamos"]:
        print("El préstamo no existe.")
        registrar_log(f"Intento de devolución de préstamo inexistente: {id_prestamo}")
        return

    prestamo = datos_prestamos["prestamos"][id_prestamo]

    # Verificar que esté activo
    if prestamo["estado"] != "activo":
        print("Este préstamo ya fue devuelto.")
        registrar_log(f"Intento de devolver préstamo ya devuelto: {id_prestamo}")
        return

    herramienta_id = prestamo["herramienta_id"]
    cantidad = prestamo["cantidad"]

    # Restaurar stock
    datos_herramientas["herramientas"][herramienta_id]["cantidad_disponible"] += cantidad

    # Cambiar estado
    prestamo["estado"] = "devuelto"

    print("Préstamo devuelto correctamente.")
    registrar_log(f"Préstamo devuelto - ID: {id_prestamo}")


def herramientas_stock_bajo(datos_herramientas):

    print("\nHerramientas con stock bajo (< 3):\n")

    for id_herramienta, info in datos_herramientas["herramientas"].items():
        if info["cantidad_disponible"] < 3:
            print(f"ID: {id_herramienta} - Nombre: {info['nombre']} - Cantidad: {info['cantidad_disponible']}")


def prestamos_activos(datos_prestamos):

    print("\nPréstamos Activos:\n")

    for id_prestamo, info in datos_prestamos["prestamos"].items():
        if info["estado"] == "activo":
            print(f"ID: {id_prestamo} - Usuario: {info['usuario_id']} - Herramienta: {info['herramienta_id']} - Cantidad: {info['cantidad']}")


def historial_usuario(datos_prestamos, usuario_id):

    print(f"\nHistorial del usuario {usuario_id}:\n")

    for id_prestamo, info in datos_prestamos["prestamos"].items():
        if info["usuario_id"] == usuario_id:
            print(f"ID: {id_prestamo} - Herramienta: {info['herramienta_id']} - Estado: {info['estado']}")


def herramientas_mas_solicitadas(datos_prestamos):

    contador = {}

    for info in datos_prestamos["prestamos"].values():
        if info["estado"] in ["activo", "devuelto"]:
            herramienta_id = info["herramienta_id"]
            cantidad = info["cantidad"]

            contador[herramienta_id] = contador.get(herramienta_id, 0) + cantidad

    if not contador:
        print("No hay datos suficientes.")
        return

    ranking = sorted(contador.items(), key=lambda x: x[1], reverse=True)

    print("\nHerramientas más solicitadas:\n")

    for herramienta_id, total in ranking:
        print(f"Herramienta {herramienta_id} - Total solicitado: {total}")


def usuarios_mas_activos(datos_prestamos):

    contador = {}

    for info in datos_prestamos["prestamos"].values():
        if info["estado"] in ["activo", "devuelto"]:
            usuario_id = info["usuario_id"]
            cantidad = info["cantidad"]

            contador[usuario_id] = contador.get(usuario_id, 0) + cantidad

    if not contador:
        print("No hay datos suficientes.")
        return

    ranking = sorted(contador.items(), key=lambda x: x[1], reverse=True)

    print("\nUsuarios más activos:\n")

    for usuario_id, total in ranking:
        print(f"Usuario {usuario_id} - Total solicitado: {total}")


def prestamos_vencidos(datos_prestamos):

    print("\nPréstamos Vencidos:\n")

    fecha_actual = datetime.today().date()

    for id_prestamo, info in datos_prestamos["prestamos"].items():

        if info["estado"] == "activo":

            try:
                fecha_devolucion = datetime.strptime(
                    info["fecha_devolucion"], "%Y-%m-%d"
                ).date()

                if fecha_devolucion < fecha_actual:
                    print(f"ID: {id_prestamo} - Usuario: {info['usuario_id']} - "
                          f"Herramienta: {info['herramienta_id']} - "
                          f"Fecha devolución: {info['fecha_devolucion']}")

            except ValueError:
                print(f"Formato de fecha inválido en préstamo {id_prestamo}")


def consultar_estado_herramienta(datos_herramientas, datos_prestamos, herramienta_id):

    if herramienta_id not in datos_herramientas["herramientas"]:
        print("La herramienta no existe.")
        return

    herramienta = datos_herramientas["herramientas"][herramienta_id]

    print("\n--- Estado de la herramienta ---")
    print(f"Nombre: {herramienta['nombre']}")
    print(f"Estado: {herramienta['estado']}")
    print(f"Cantidad disponible: {herramienta['cantidad_disponible']}")

    print("\nPréstamos activos asociados:\n")

    encontrada = False

    for id_prestamo, info in datos_prestamos["prestamos"].items():
        if (info["herramienta_id"] == herramienta_id and 
            info["estado"] == "activo"):

            print(f"Préstamo ID: {id_prestamo}")
            print(f"Usuario: {info['usuario_id']}")
            print(f"Cantidad: {info['cantidad']}")
            print(f"Fecha estimada devolución: {info['fecha_devolucion']}")
            print("---------------------------")

            encontrada = True

    if not encontrada:
        print("No hay préstamos activos para esta herramienta.")
