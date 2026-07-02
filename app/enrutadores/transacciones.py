from fastapi import APIRouter, HTTPException, status
from ..modelos.transacciones import Transaccion, TransaccionCrear, TransaccionEditar
from ..modelos.facturas import Factura
from ..listas import lista_facturas, lista_transacciones

rutas_transacciones = APIRouter()

# lista_facturas:list[Factura]
# lista_transacciones:list[Transaccion]

#crear endpoints para transacciones

@rutas_transacciones.get("/transacciones", response_model=list[Transaccion])
async def listar_transacciones():
    return lista_transacciones

@rutas_transacciones.get("/transacciones/{id_transaccion}", response_model=Transaccion)
async def listar_transaccion(id_transaccion: int):
    for i, obj_transaccion in enumerate(lista_transacciones):
        if obj_transaccion.id == id_transaccion:
            return obj_transaccion
        
@rutas_transacciones.post("/transacciones/{factura_id}", response_model=Transaccion)
async def crear_transaccion(factura_id: int, datos_transaccion: TransaccionCrear):
    #buscar la factura
    factura_encontrada = None
    for factura in lista_facturas:
        if factura.id == factura_id:
            factura_encontrada = factura
    #mensaje si la factura no existe
    if not factura_encontrada:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"La factura con id {factura_id} no existe"
        )
    
    #validar datos
    transaccion_val = Transaccion.model_validate(datos_transaccion.model_dump())
    transaccion_val.factura_id = factura_id
    factura_encontrada.transacciones.append(transaccion_val)
    #id de la transaccion
    transaccion_val.id = len(lista_transacciones) + 1
    lista_transacciones.append(transaccion_val)
    return transaccion_val

@rutas_transacciones.patch("/transacciones/{id_transaccion}", response_model=Transaccion)
async def editar_transaccion(id_transaccion:int, datos_transaccion: TransaccionEditar):
    for i, obj_transaccion in enumerate(lista_transacciones):
        if obj_transaccion.id == id_transaccion:
            #validar transaccion
            transaccion_val = Transaccion.model_validate(datos_transaccion.model_dump())
            transaccion_val.id = id_transaccion