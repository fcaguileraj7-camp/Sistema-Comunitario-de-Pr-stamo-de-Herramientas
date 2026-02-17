"""
Este módulo se encarga de gestionar los datos json en el disco
"""
import json

# ------------------ HERRAMIENTAS ------------------

def cargar_datos_herramientas(nom_archivo="herramientas.json"):
    try:
        with open(nom_archivo, "r") as arch:
            return json.load(arch)
    except FileNotFoundError:
        return {"herramientas": {}}

def guardar_datos_herramientas(datos, nom_archivo="herramientas.json"):
    with open(nom_archivo, "w") as arch:
        json.dump(datos, arch, indent=4)


# ------------------ USUARIOS ------------------

def cargar_datos_usuarios(nom_archivo="usuarios.json"):
    try:
        with open(nom_archivo, "r") as arch:
            return json.load(arch)
    except FileNotFoundError:
        return {"usuarios": {}}

def guardar_datos_usuarios(datos, nom_archivo="usuarios.json"):
    with open(nom_archivo, "w") as arch:
        json.dump(datos, arch, indent=4)


# ------------------ PRESTAMOS ------------------

def cargar_datos_prestamos(nom_archivo="prestamos.json"):
    try:
        with open(nom_archivo, "r") as arch:
            return json.load(arch)
    except FileNotFoundError:
        return {"prestamos": {}}

def guardar_datos_prestamos(datos, nom_archivo="prestamos.json"):
    with open(nom_archivo, "w") as arch:
        json.dump(datos, arch, indent=4)
