# Cotizaciones con DolarAPI

Este proyecto consulta la cotización del dólar oficial y dólar blue en pesos argentinos,
utilizando la API pública [DolarAPI.com](https://dolarapi.com).

## Funcionalidad
- Obtiene las cotizaciones en tiempo real.
- Muestra valores de compra y venta con fecha y hora.
- Código modular y documentado siguiendo PEP8 y PEP257.

## Requisitos del sistema
- Python 3.10 o superior.
- Conexión a internet.
- Sistema operativo: Windows, Linux o MacOS.

## Instalación y entorno virtual (venv)

1. El repositorio:
   ```bash
   git clone https://github.com/NahuelSchwab/cotizaciones_dolarapi.git
   cd cotizaciones_dolarapi

   Entorno virtual:
   python -m venv venv

   Activar entorno virtual:
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass .\venv\Scripts\Activate

   Linux/Mac :
   source venv/bin/activate

   instalar dependencias:
    pip install -r requirements.txt

