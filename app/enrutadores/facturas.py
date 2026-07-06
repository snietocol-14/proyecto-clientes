from fastapi import APIRouter, HTTPException, status
from ..modelos.facturas import Factura, FacturaCrear, FacturaEditar, FacturaLeer, FacturaLeerCompuesta
from ..modelos.clientes import Cliente
from ..listas import lista_clientes, lista_facturas
from ..conexion_bd import Sesion_dependencia
from sqlmodel import select

rutas_facturas = APIRouter()

# lista_clientes:list[Cliente] = []#vacía
# lista_facturas:list[Factura] = []


@rutas_facturas.get("/facturas", response_model=list[FacturaLeerCompuesta])
async def listar_facturas(sesion: Sesion_dependencia):
    #select * from factura
    consulta = select(Factura)
    lista_facturas = sesion.exec(consulta).all()
    return lista_facturas

@rutas_facturas.get("/facturas/{id_factura}", response_model=Factura)
async def listar_factura(id_factura: int):
    #recorrer la lista_facturas
    for i, obj_factura in enumerate(lista_facturas):
        if obj_factura.id == id_factura:
            return obj_factura
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=f"La factura con id {id_factura} no existe"
        )

@rutas_facturas.post("/facturas", response_model=Factura)
async def crear_factura(cliente_id: int, datos_factura: FacturaCrear, sesion:Sesion_dependencia):
    #buscar el cliente
    cliente_encontrado = sesion.get(Cliente, cliente_id)
    if not cliente_encontrado:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El cliente con id {cliente_id} no existe"
        )
    
    #validar datos de factura-json, pasar dict
    factura_dict = datos_factura.model_dump()
    factura_dict["cliente_id"] = cliente_id
    factura_val = Factura.model_validate(factura_dict)
    
    #guardar en bd
    sesion.add(factura_val)
    sesion.commit()
    sesion.refresh(factura_val)
    return factura_val

@rutas_facturas.patch("/facturas/{id_factura}", response_model=Factura)
async def editar_factura(id_factura:int, datos_factura: FacturaEditar):
    for i, obj_factura in enumerate(lista_facturas):
        if obj_factura.id == id_factura:
            #validar factura
            factura_val = Factura.model_validate(datos_factura.model_dump())
            factura_val.id = id_factura
            lista_facturas[i] = factura_val
            return factura_val
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=f"La factura con id {id_factura} no existe"
    )

@rutas_facturas.delete("/facturas/{id_factura}", response_model=Factura)
async def eliminar_factura(id_factura:int):
    pass
