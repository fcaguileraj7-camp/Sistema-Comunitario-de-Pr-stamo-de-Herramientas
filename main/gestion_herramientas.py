def agregar_herramienta(datos, id_herramienta, categoria, cantidad_disponible, estado, valor_estimado):

    if id_herramienta in datos:
        print(f"La herramienta con ID {id_herramienta} ya esta creada.")
        return
    
    datos["herramientas"][id_herramienta] = {
        "categoria": categoria,
        "cantidad_disponible": cantidad_disponible,
        "estado": estado,
        "valor_estimado": valor_estimado
    }

    datos[id_herramienta] = categoria, cantidad_disponible, estado, valor_estimado
    print(f"\n\nHerramienta {id_herramienta} agregada exitosamente.\n\n") or {}

def listar_herramienta(datos):
    if not datos:
        print("No hay herramientas registradas.")

    else:
        for id_herramienta, (categoria, cantidad_disponible, estado, valor_estimado) in datos.items():
            print(f"ID: {id_herramienta}, Categoria: {categoria}, Cantidad Disponible: {cantidad_disponible}, Estado: {estado}, Valor Estimado: {valor_estimado}")

def buscar_herramienta(datos, id_herramienta):
    if id_herramienta in datos:
        print(f"ID: {id_herramienta}, Categoria: {datos[id_herramienta][0]}, Cantidad Disponible: {datos[id_herramienta][1]}, Estado: {datos[id_herramienta][2]}, Valor Estimado: {datos[id_herramienta][3]}")
    else:
        print("Herramienta no encontrada.")

def actualizar_herramientas(datos, id_herramienta, categoria, cantidad, disponibilidad):
    if id_herramienta in datos:
        datos[id_herramienta] = categoria, cantidad, disponibilidad
        print("Herramienta actualizada correctamente.")
    else:
        print("Herramienta no encontrada.")

def activar_inactivar(datos, id_herramienta):
    if id_herramienta in datos:
        if datos[id_herramienta][3] == "Activa":
            datos[id_herramienta] = datos[id_herramienta][0], datos[id_herramienta][1], datos[id_herramienta][2], "Inactiva"
            print("Herramienta inactivada.")
        else:
            datos[id_herramienta] = datos[id_herramienta][0], datos[id_herramienta][1], datos[id_herramienta][2], "Activa"
            print("Herramienta activada.")
    else:
        print("Herramienta no encontrada.")

def eliminar_herramienta(datos, id_herramienta):
    if id_herramienta in datos:
        del datos[id_herramienta]
        print("Herramienta eliminada correctamente.")
    else:
        print("Herramienta no encontrada.")


