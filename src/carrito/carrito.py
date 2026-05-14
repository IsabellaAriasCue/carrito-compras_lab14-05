from .modelos import Producto


class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)

    def calcular_total(self):
        return sum(producto.precio * producto.cantidad for producto in self.productos)