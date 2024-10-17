import json
from datetime import datetime

# Cargar datos del archivo JSON
def cargar_datos(archivo):
    with open(archivo, 'r') as f:
        return json.load(f)

# Generar reporte HTML
def generar_reporte(cliente):
    html = f'''
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <title>Reporte de Transacciones para {cliente['nombre']}</title>
      <style>
        table {{ width: 100%; border-collapse: collapse; }}
        th, td {{ border: 1px solid #ccc; padding: 8px; text-align: left; }}
        th {{ background-color: #f2f2f2; }}
      </style>
    </head>
    <body>
      <h1>Reporte de Transacciones para {cliente['nombre']}</h1>
      <p>DNI: {cliente['DNI']}</p>
      <p>Tipo: {cliente['tipo']}</p>
      <table>
        <tr>
          <th>Fecha</th>
          <th>Tipo de Operación</th>
          <th>Estado</th>
          <th>Monto</th>
          <th>Razón</th>
        </tr>'''

    for transaccion in cliente['transacciones']:
        html += f'''
        <tr>
          <td>{transaccion['fecha']}</td>
          <td>{transaccion['tipo']}</td>
          <td>{transaccion['estado']}</td>
          <td>{transaccion['monto']}</td>
          <td>{transaccion['razon']}</td>
        </tr>'''
    
    html += '''
      </table>
    </body>
    </html>
    '''
    
    return html

# Guardar el reporte HTML
def guardar_reporte(html, nombre_archivo):
    with open(nombre_archivo, 'w') as f:
        f.write(html)

# Función principal
def main():
    datos = cargar_datos('transacciones.json')
    reporte_html = generar_reporte(datos)
    guardar_reporte(reporte_html, 'reporte.html')
    print("Reporte generado: reporte.html")

if __name__ == "__main__":
    main()
