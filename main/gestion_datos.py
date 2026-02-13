"""
Este módulo se encarga de gestionar los datos json en
el disco
"""
import json

def cargar_datos_herramientas(nom_archivo="herramientas.json"):
    try:
        with open(nom_archivo, "r") as arch:
            return json.load(arch)
    except FileNotFoundError:
        return {}
    
def guardar_datos_herramientas(datos, nom_archivo="herramientas.json"):
    try:
        with open(nom_archivo, "w") as arch:
            json.dump(datos, arch)
    except Exception:
        datos = {}

def cargar_datos_usuarios(nom_archivo="usuarios.json"):
    try:
        with open(nom_archivo, "r") as arch:
            return json.load(arch)
    except FileNotFoundError:
        return {}

def guardar_datos_usuarios(datos, nom_archivo="usuarios.json"):
    try:
        with open(nom_archivo, "w") as arch:
            json.dump(datos, arch)
    except Exception:
        datos = {}

def cargar_datos_prestamos(nom_archivo="prestamos.json"):
    try:
        with open(nom_archivo, "r") as arch:
            return json.load(arch)
    except FileNotFoundError:
        return {}

def guardar_datos_prestamos(datos, nom_archivo="prestamos.json"):
    try:
        with open(nom_archivo, "w") as arch:
            json.dump(datos, arch)
    except Exception:
        datos = {}