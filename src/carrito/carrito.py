from .modelos import Producto


class Carrito:
    def __init__(self):
        self.productos = []
        self.tipo_cupon = None
        self.valor_cupon = 0

    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)

    def aplicar_cupon(self, tipo, valor):
        self.tipo_cupon = tipo
        self.valor_cupon = valor

    def calcular_total(self):
        subtotal = sum(
            producto.precio * producto.cantidad
            for producto in self.productos
        )

        if self.tipo_cupon == "porcentaje":
            return subtotal * (1 - self.valor_cupon / 100)

        return subtotal