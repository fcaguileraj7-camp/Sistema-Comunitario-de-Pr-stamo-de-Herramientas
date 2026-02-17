from datetime import datetime


def registrar_log(mensaje):

    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("logs.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"[{fecha_hora}] {mensaje}\n")
