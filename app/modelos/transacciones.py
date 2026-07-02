from pydantic import BaseModel

#crear el modelo transaccion
class TransaccionBase(BaseModel):
    cantidad: int
    vr_unitario: float
    factura_id: int

class TransaccionCrear(TransaccionBase):
    pass

class TransaccionEditar(TransaccionBase):
    pass

class Transaccion(TransaccionBase):
    id: int | None = None
    #aquí va la relación con el modelo cliente (solo un campo)
