from pydantic import computed_field
from sqlmodel import SQLModel, Field, Relationship
from .transacciones import Transaccion
from .clientes import Cliente, ClienteLeer
from datetime import datetime

class FacturaBase(SQLModel):
    fecha: str = Field(default=datetime.now())

class FacturaCrear(FacturaBase):
    pass

class FacturaEditar(FacturaBase):
    pass

class Factura(FacturaBase, table=True):
    id:int | None = Field(default=None, primary_key=True)
    cliente_id: int = Field(default=None, foreign_key="cliente.id")
    #crear relaciones virtuales con cliente, transacciones
    cliente: Cliente = Relationship(back_populates="factura")
    transacciones: list[Transaccion] = Relationship(back_populates="factura")

    @computed_field
    @property
    def vr_total(self) -> float:
        # total_factura = 0.0
        # if self.transacciones == None:
        #     return total_factura
        # # recorrer la lista de transacciones
        # for transaccion in self.transacciones:
        #     total_factura += transaccion.cantidad * transaccion.vr_unitario
        return 0.0

#crear modelo para mostrar la usuario o el cliente
class FacturaLeer(FacturaBase):
    id:int
    cliente:ClienteLeer

class FacturaLeerCompuesta(FacturaLeer):
    transacciones:list[Transaccion] = []

