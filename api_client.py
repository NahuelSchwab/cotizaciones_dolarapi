"""
Módulo api_client
-----------------
Consulta las cotizaciones del dólar oficial y dólar blue desde la API de DolarAPI.
"""

import requests


def obtener_cotizaciones_dolarapi() -> dict:
    """
    Obtiene las cotizaciones del dólar oficial y dólar blue desde dolarapi.com.

    Returns
    -------
    dict
        Diccionario con las cotizaciones de compra y venta.
    """
    url = "https://dolarapi.com/v1/dolares"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()

    cotizaciones = {}
    for item in data:
        nombre = item["nombre"]
        if nombre == "Oficial":
            cotizaciones["Dólar Oficial"] = {
                "compra": item["compra"],
                "venta": item["venta"]
            }
        elif nombre == "Blue":
            cotizaciones["Dólar Blue"] = {
                "compra": item["compra"],
                "venta": item["venta"]
            }

    return cotizaciones




