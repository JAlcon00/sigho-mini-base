REGLAS_PRECIO = {
    "electronica": {
        "umbral_1": 4,
        "descuento_1": 0.10,
        "umbral_2": 8,
        "descuento_2": 0.15,
        "impuesto": 0.16,
    },
    "ropa": {
        "umbral_1": 5,
        "descuento_1": 0.10,
        "umbral_2": 10,
        "descuento_2": 0.15,
        "impuesto": 0.16,
    },
    "alimentos": {
        "umbral_1": 20,
        "descuento_1": 0.05,
        "umbral_2": None,
        "descuento_2": 0.0,
        "impuesto": 0.08,
    },
}


def _aplicar_descuento(subtotal, cantidad, regla):
    if regla["umbral_2"] is not None and cantidad > regla["umbral_2"]:
        descuento = subtotal * regla["descuento_2"]
    elif cantidad > regla["umbral_1"]:
        descuento = subtotal * regla["descuento_1"]
    else:
        descuento = 0
    return descuento


def calcular_precio_final(precio, cantidad, categoria):
    regla = REGLAS_PRECIO.get(categoria)
    if regla is None:
        return precio * cantidad

    subtotal = precio * cantidad
    descuento = _aplicar_descuento(subtotal, cantidad, regla)
    total = subtotal - descuento
    return total + (total * regla["impuesto"])