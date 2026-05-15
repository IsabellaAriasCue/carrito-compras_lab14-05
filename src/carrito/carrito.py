from .modelos import Producto


class Carrito:
    def __init__(self):
        self.productos = []
        self.descuento = 0

    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)

    def aplicar_cupon(self, tipo, valor):
        if tipo == "porcentaje":
            self.descuento = valor / 100

    def calcular_total(self):
        subtotal = sum(
            producto.precio * producto.cantidad
            for producto in self.productos
        )
        return subtotal * (1 - self.descuento)