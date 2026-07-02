from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Relationship

#crear el modelo clientes
class ClienteBase(BaseModel):
    nombre:str = Field(default=None)
    email:str = Field(default=None)
    descripcion:str 

class ClienteCrear(ClienteBase):
    pass

class ClienteEditar(ClienteBase):
    pass

class Cliente(ClienteBase, table=True):
    id:int | None = Field(default=None, primary_key=True)