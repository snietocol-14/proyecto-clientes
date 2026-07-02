from fastapi import FastAPI, Depends
from typing import Annotated
from sqlmodel import Session, create_engine, SQLModel

nombre_bd = "bd_clientes.sqlite3"
url_bd = f"sqlite:///{nombre_bd}"

#motor de bd
motor_bd = create_engine(url_bd)

#definir método para crear las tablas
def crear_tablas():
    SQLModel.metadata.create_all(motor_bd)
    yield

#definir método para la sesión
def obtener_sesion():
    with Session(motor_bd) as mi_sesion:
        yield mi_sesion#retorna la sesión

#inyección de dependencias
#registrar la sesion como dependencia utilizada en los endpoints
Sesion_dependencia = Annotated[Session, Depends(obtener_sesion)]
