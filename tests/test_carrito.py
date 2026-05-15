from carrito.carrito import Carrito
from carrito.modelos import Producto


def test_aplicar_cupon_porcentaje():
    carrito = Carrito()
    carrito.agregar_producto(Producto("Laptop", 100000, 1))

    carrito.aplicar_cupon(tipo="porcentaje", valor=15)

    assert carrito.calcular_total() == 85000

def test_vaciar_carrito():
    carrito = Carrito()

    carrito.agregar_producto(Producto("Laptop", 100000, 1))
    carrito.agregar_producto(Producto("Mouse", 50000, 1))

    carrito.vaciar()

    assert len(carrito.productos) == 0
    assert carrito.calcular_total() == 0