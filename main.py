from fastapi import FastAPI, HTTPException
from modelos.cliente import Cliente, ClienteCrear, ClienteEditar

app = FastAPI()

lista_clientes:list[Cliente] = []

#listar todos los clientes
@app.get("/clientes", response_model=list[Cliente])
async def listar_clientes():
    return lista_clientes

#listar un solo cliente
@app.get("/clientes/{cliente_id}", response_model=Cliente)
async def listar_cliente(cliente_id: int):
    #recorrer la lista_clientes
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.get("id") == cliente_id:
            return obj_cliente

#crear un cliente y agregarlo a la lista
@app.post("/clientes", response_model=Cliente)
async def crear_cliente(datos_cliente : ClienteCrear):
    cliente_val = Cliente.model_validate(datos_cliente.model_dump())
    #generar id
    id_cliente = len(lista_clientes) + 1
    cliente_val.id = id_cliente
    lista_clientes.append(cliente_val)
    return cliente_val

#editar un cliente
@app.patch("/clientes/{id}", response_model=Cliente)
async def editar_cliente(cliente_id:int, datos_cliente: ClienteEditar):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            #validar cliente
            cliente_val = Cliente.model_validate(datos_cliente.model_dump())
            listar_cliente[i] = datos_cliente
            return obj_cliente
        raise HTTPException(
            status_code=400, detail=f"El cliente con id {cliente_id} no existe"
        )

@app.delete("/clientes/{id}")
async def eliminar_cliente(id:int):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == id:
            lista_clientes.pop(i)
            return {"mensaje": "Cliente eliminado satisfactoriamente.","eliminado": obj_cliente}
    return {"error": "Cliente no encontrado"}


            
