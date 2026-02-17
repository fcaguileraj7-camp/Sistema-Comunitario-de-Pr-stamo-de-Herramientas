# Sistema Comunitario de Préstamo de Herramientas

## Descripción del Proyecto

Este proyecto consiste en el desarrollo de un programa de consola en Python para gestionar el préstamo de herramientas dentro de una comunidad.

El sistema permite registrar usuarios, herramientas y préstamos, con el objetivo de organizar el control de disponibilidad, evitar pérdidas y llevar un seguimiento adecuado de las herramientas compartidas entre vecinos.

---

## Objetivo

Brindar una solución digital básica que permita:

- Registrar herramientas y usuarios.
- Gestionar solicitudes de préstamo.
- Aprobar o rechazar solicitudes.
- Registrar devoluciones.
- Consultar reportes.
- Llevar registro de eventos en un archivo de logs.

---

## Estructura del Proyecto

El proyecto está organizado en módulos:

- `main.py` → Archivo principal del sistema.
- `gestion_usuarios.py` → Lógica de usuarios.
- `gestion_herramientas.py` → Lógica de herramientas.
- `gestion_prestamos.py` → Lógica de préstamos y reportes.
- `gestion_datos.py` → Manejo de archivos JSON.
- `gestion_logs.py` → Registro de eventos en archivo de texto.
- `menu_usuarios.py` → Menú de gestión de usuarios.
- `menu_herramientas.py` → Menú de gestión de herramientas.
- `menu_prestamos.py` → Menú de gestión de préstamos.
- Carpeta `pruebas/` → Casos de prueba documentados.

---

## Persistencia de Datos

El sistema utiliza archivos JSON para almacenar la información:

- `usuarios.json`
- `herramientas.json`
- `prestamos.json`

Los datos se guardan cuando se selecciona la opción "Guardar y salir" en cada módulo.

---

## Roles del Sistema

### Administrador

Puede:

- Crear, listar, actualizar e inactivar usuarios.
- Crear, listar, actualizar e inactivar herramientas.
- Ver solicitudes pendientes.
- Aprobar o rechazar solicitudes.
- Registrar devoluciones.
- Consultar reportes.

### Usuario

Puede:

- Consultar estado de herramientas.
- Crear solicitudes de préstamo (pendientes de aprobación).

---

## Flujo del Sistema

1. El usuario crea una solicitud de préstamo.
2. La solicitud queda en estado "pendiente".
3. El administrador puede:
   - Aprobar la solicitud (cambia a "activo" y descuenta stock).
   - Rechazar la solicitud.
4. Cuando se devuelve la herramienta, el préstamo cambia a "devuelto" y el stock se restaura.

---

## Reportes Disponibles

El sistema permite consultar:

- Herramientas con stock bajo.
- Préstamos activos.
- Préstamos vencidos.
- Historial de préstamos por usuario.
- Herramientas más solicitadas (ordenadas).
- Usuarios más activos (ordenados).

---

## Registro de Eventos (Logs)

El sistema genera un archivo `logs.txt` donde se registran eventos importantes como:

- Intentos de creación duplicada.
- Solicitudes inválidas.
- Aprobaciones.
- Rechazos.
- Errores de stock.

---

## Cómo Ejecutar el Programa

1. Asegurarse de tener Python instalado.
2. Ubicarse en la carpeta del proyecto.
3. Ejecutar: python main.py
4. Seleccionar el rol (Administrador o Usuario).
5. contraseña Administrador: 123456
5. Navegar por el menú según la opción deseada.

---

## Consideraciones Finales

- El sistema trabaja únicamente por consola.
- No utiliza base de datos externa.
- Toda la información se almacena en archivos locales JSON.
- Se implementó validación básica para evitar inconsistencias.
- Los usuarios y herramientas pueden inactivarse en lugar de eliminarse para conservar el historial.
