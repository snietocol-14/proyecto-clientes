from pydantic import computed_field
from sqlmodel import SQLModel, Field, Relationship
from modelos.clientes import Cliente
from datetime import datetime

class FacturaBase(SQLModel):
    fecha: str = datetime.now()
    cliente: Cliente

    @computed_field
    @property
    def vr_total(self) -> float:
        #calcular (cantidad*vr_unitario)
        #consultar el id actual de factura
        factura_id_actual = getattr(self, "id", None)
        total_factura = 0.0
        if not factura_id_actual or not self.transacciones:
            return total_factura
        #recorrer la lista de transacciones según el factura_id
        for transaccion in self.transacciones:
            if transaccion.factura_id == factura_id_actual:
                total_factura += transaccion.cantidad * transaccion.vr_unitario
        return total_factura

class FacturaCrear(FacturaBase):
    pass

class FacturaEditar(FacturaBase):
    pass

class Factura(FacturaBase):
    id:int | None = None