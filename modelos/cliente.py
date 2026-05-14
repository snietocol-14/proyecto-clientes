from pydantic import BaseModel

class Cliente(BaseModel):
    id:int = 0
    nombre:str
    edad:int
    descripcion:str | None=None