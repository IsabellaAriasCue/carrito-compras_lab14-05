from dataclasses import dataclass


@dataclass
class Producto:
    nombre: str
    precio: float
    cantidad: int = 1