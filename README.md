# Proyecto: Gestión de Clientes y Facturas

Resumen
-------
Pequeña aplicación en Python para gestionar clientes, facturas y transacciones usando una base de datos SQLite.

Caracteristicas principales
--------------------------
- Gestión de clientes 
- Gestión de facturas vinculadas a clientes
- Registro de transacciones
- API modularizada en enrutadores separados: `clientes`, `facturas`, `transacciones`
- La API queda disponible en http://127.0.0.1:8000 por defecto.

Estructura del proyecto
-----------------------
Raíz del proyecto:

```
bd_clientes.sqlite3
pyproject.toml
README.md
app/
	__init__.py
	conexion_bd.py
	listas.py
	main.py
	enrutadores/
		__init__.py
		clientes.py
		facturas.py
		transacciones.py
modelos/
	__init__.py
	clientes.py
	facturas.py
	transacciones.py
```

Requisitos
----------
- Python 3.9+
- Dependencias descritas en el pyproject.toml (ejecutar uv sync)

Base de datos
-------------
- El proyecto usa `bd_clientes.sqlite3` en la raíz como almacenamiento.
- Las conexiones y utilidades relacionadas se encuentran en `app/conexion_bd.py`.

Rutas / Enrutadores
-------------------
Las rutas HTTP están organizadas en `app/enrutadores/`:
- `clientes.py` — operaciones relacionadas con clientes.
- `facturas.py` — operaciones relacionadas con facturas.
- `transacciones.py` — operaciones relacionadas con transacciones.

Para ver los endpoints exactos y ejemplos de uso, abra los archivos en `app/enrutadores/`.

Autor
-----
Anggy Sofia Nieto Colmenares — 3407184


