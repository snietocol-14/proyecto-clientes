from fastapi import APIRouter, HTTPException
from ..modelos.clientes import Cliente, ClienteCrear, ClienteEditar
from ..listas import lista_clientes 
from ..conexion_bd import Sesion_dependencia

rutas_clientes = APIRouter()
# lista_clientes:list[Cliente] = []

#listar todos los clientes
@rutas_clientes.get("/clientes", response_model=list[Cliente])
async def listar_clientes():
    return lista_clientes

#listar un solo cliente
@rutas_clientes.get(
    "/clientes/{cliente_id}",
    response_model=Cliente,
)
async def listar_cliente(cliente_id: int, mi_sesion: Sesion_dependencia):
    #recorrer la lista_clientes
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.get("id") == cliente_id:
            return obj_cliente
    raise HTTPException(
        status_code=400, detail=f"El cliente con id {cliente_id} no existe"
    )

#crear un cliente y agregarlo a la lista
@rutas_clientes.post("/clientes", response_model=Cliente)
async def crear_cliente(datos_cliente: ClienteCrear, mi_sesion: Sesion_dependencia):
    cliente_val = Cliente.model_validate(datos_cliente.model_dump())
    mi_sesion.add(cliente_val)
    mi_sesion.commit()
    mi_sesion.refresh(cliente_val)
    return cliente_val

#editar un cliente
@rutas_clientes.patch("/clientes/{id}", response_model=Cliente)
async def editar_cliente(cliente_id:int, datos_cliente: ClienteEditar):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            #validar cliente
            cliente_val = Cliente.model_validate(datos_cliente.model_dump())
            cliente_val.id = cliente_id
            listar_clientes[i] = cliente_val
            return cliente_val
    raise HTTPException(
        status_code=400, detail=f"El cliente con id {cliente_id} no existe"
    )

@rutas_clientes.delete("/clientes/{cliente_id}", response_model=Cliente)
async def eliminar_cliente(cliente_id:int):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            cliente_eliminado = lista_clientes.pop(i)
            return cliente_eliminado
    raise HTTPException(
        status_code=400, detail=f"El cliente con id {cliente_id} no existe"
    )