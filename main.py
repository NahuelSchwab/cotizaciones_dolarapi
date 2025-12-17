"""
Programa principal
------------------
Consulta diariamente la cotización del dólar oficial y dólar blue en pesos argentinos
desde la API de DolarAPI
"""

from api_client import obtener_cotizaciones_dolarapi
from utils import formatear_salida


def main():
    """Función principal del programa
       Obtiene las cotizaciones y las imprime en consola formateadas"""
    datos = obtener_cotizaciones_dolarapi()

    oficial = datos.get("Dólar Oficial")
    blue = datos.get("Dólar Blue")

    if oficial:
        print(formatear_salida("Dólar Oficial", oficial["compra"], oficial["venta"]))
    if blue:
        print(formatear_salida("Dólar Blue", blue["compra"], blue["venta"]))


if __name__ == "__main__":
    main()

