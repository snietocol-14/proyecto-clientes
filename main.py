from fastapi import FastAPI
from modelos.cliente import Cliente

app = FastAPI()
lista_clientes:list[Cliente] = []
contador_id = 0

@app.get("/clientes")
def listar_clientes():
    return {"Clientes": lista_clientes}

@app.post("/clientes")
def crear_clientes(datos_cliente : Cliente):
    global contador_id
    contador_id += 1
    datos_cliente.id = contador_id
    lista_clientes.append(datos_cliente)
    return {"mensaje":"Cliente creado"}

@app.get("/clientes/{cliente_id}")
def obtener_cliente(cliente_id: int):
    for cliente in lista_clientes:
        if cliente.id == cliente_id:
            return cliente
    return {"error" : "Cliente no encontrado"}

@app.put("/clientes/{id}")
def editar_cliente(id:int, datos_cliente: Cliente):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == id:
            cliente_val = Cliente.model_validate(datos_cliente.model_dump())
            cliente_val.id = id
            lista_clientes[i] = cliente_val
            return {"mensaje":"Se actualizó el cliente satisfactoriamente.","Cliente": cliente_val}
    return {"error": "Cliente no encontrado"}

@app.delete("/clientes/{id}")
def eliminar_cliente(id:int):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == id:
            lista_clientes.pop(i)
            return {"mensaje": "Cliente eliminado satisfactoriamente.","eliminado": obj_cliente}
    return {"error": "Cliente no encontrado"}


            
