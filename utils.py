"""
Módulo utils:

Funciones auxiliares para formatear y mostrar resultados.
"""

from datetime import datetime


def formatear_salida(moneda: str, compra: float, venta: float) -> str:
    """
    Devuelve un string formateado con la cotización.

    Parametros
    ----------
    moneda : str
    Nombre de la moneda.
    compra : float
    Valor de compra.
    venta : float
    Valor de venta.

    Returns
    -------
    str
        Texto formateado con fecha y valores.
    """
    fecha = datetime.now().strftime("%d-%m-%Y %H:%M")
    return f"[{fecha}] {moneda}: Compra ${compra:.2f} - Venta ${venta:.2f}"



