# Carrito de Compras con TDD

Proyecto académico desarrollado en Python para practicar la metodología **Test-Driven Development (TDD)** mediante la implementación incremental de funcionalidades de un carrito de compras.

## Objetivo

Aplicar la metodología TDD siguiendo el ciclo:

1. **Red**: escribir una prueba que falle.
2. **Green**: implementar el código mínimo para que la prueba pase.
3. **Refactor**: mejorar el diseño sin alterar el comportamiento.

## Requisitos Implementados

### RF4 – Aplicar descuentos por cupón

Permite aplicar descuentos al total del carrito mediante un cupón de tipo porcentaje.

**Ejemplo:**

* Total inicial: $100.000
* Cupón: 15%
* Total final: $85.000

### RF7 – Vaciar el carrito

Permite eliminar todos los productos del carrito en una sola operación.

## Estructura del Proyecto

```text
carrito-compras/
│
├── src/
│   └── carrito/
│       ├── __init__.py
│       ├── modelos.py
│       └── carrito.py
│
└── tests/
    ├── conftest.py
    └── test_carrito.py
```

## Tecnologías Utilizadas

* Python 3.12
* pytest
* PyCharm

## Metodología Aplicada

### RF4 – Aplicar descuentos por cupón

* Red: se creó el test `test_aplicar_cupon_porcentaje`
* Green: se implementó `aplicar_cupon`
* Refactor: se mejoró el diseño usando `tipo_cupon` y `valor_cupon`

### RF7 – Vaciar el carrito

* Red: se creó el test `test_vaciar_carrito`
* Green: se implementó `vaciar`
* Refactor: no fue necesario realizar cambios adicionales

## Aprendizajes Obtenidos

* Desarrollo guiado por pruebas
* Diseño incremental de software
* Refactorización segura
* Automatización de pruebas con pytest
* Aplicación de buenas prácticas de programación

## Autor

Isabela Arias Lemus
Ingeniería de Software
Corporación Universitaria Empresarial Alexander von Humboldt
