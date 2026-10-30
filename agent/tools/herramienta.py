def obtener_clima(ciudad: str) -> dict:
    """
    Devuelve el clima actual de una ciudad.

    """
    climas = {
        "Madrid": {"temp": "22°C", "cond": "Soleado"},
        "Bogotá": {"temp": "18°C", "cond": "Nublado"},
    }
    datos = climas.get(ciudad, {"temp": "Desconocida", "cond": "Desconocido"})
    return { "ciudad": ciudad, ** datos}

