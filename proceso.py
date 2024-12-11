import json
from datetime import datetime

# Cargar datos del archivo JSON
def cargar_datos(archivo):
    with open(archivo, 'r') as f:
        return json.load(f)

# Formatear la fecha
def formatear_fecha(fecha):
    return datetime.strptime(fecha, "%d/%m/%Y %H:%M:%S").strftime("%d/%m/%Y")

# Generar reporte HTML
def generar_reporte(clientes):
    html = '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <title>Reportes de Transacciones</title>
      <style>
        body {
      font-family: 'Roboto', Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f0f2f5;
      color: #333;
      line-height: 1.6;
    }
    header {
      background-color: #004080;
      color: #fff;
      padding: 20px;
      text-align: center;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    header h1 {
      margin: 0;
      font-size: 2rem;
    }
    .container {
      max-width: 1200px;
      margin: 20px auto;
      background: #fff;
      border-radius: 8px;
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
      padding: 20px;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      margin: 20px 0;
    }
    th, td {
      border: 1px solid #ddd;
      padding: 12px;
      text-align: left;
    }
    th {
      background-color: #004080;
      color: #fff;
      text-transform: uppercase;
      font-size: 0.9rem;
    }
    tr:nth-child(even) {
      background-color: #f9f9f9;
    }
    tr:hover {
      background-color: #f1f5ff;
    }
    .rechazada {
      background-color: #ffcccc !important;
      color: #b30000;
    }
    .info {
      background-color: #e6f7ff;
      color: #004080;
    }
    footer {
      text-align: center;
      padding: 10px;
      margin-top: 20px;
      background-color: #f0f2f5;
      font-size: 0.85rem;
      color: #666;
    }
      </style>
    </head>
    <body>
      <h1>Reportes de Transacciones</h1>
    '''

    for cliente in clientes:
        total_transacciones = len(cliente['transacciones'])
        aceptadas = sum(1 for t in cliente['transacciones'] if t['estado'] == 'ACEPTADA')
        rechazadas = total_transacciones - aceptadas

        html += f'''
        <h2>Cliente: {cliente['nombre']} {cliente['apellido']} (DNI: {cliente['DNI']})</h2>
        <div>
          <strong>Tipo de Cliente:</strong> {cliente['tipo']}<br>
          <strong>Tarjetas de Credito:</strong> {cliente['totalTarjetasDeCreditoActualmente']}<br>
          <strong>Chequeras:</strong> {cliente['totalChequerasActualmente']}<br>
          <strong>Resumen de Transacciones:</strong><br>
          Total de transacciones: {total_transacciones}<br>
          Transacciones aceptadas: {aceptadas}<br>
          Transacciones rechazadas: {rechazadas}
        </div>
        <table>
          <tr>
            <th>Fecha</th>
            <th>Tipo de Operacion</th>
            <th>Estado</th>
            <th>Monto</th>
            <th>Razón</th>
          </tr>'''

        for transaccion in cliente['transacciones']:
            estado_clase = "rechazada" if transaccion['estado'] == "RECHAZADA" else ""
            html += f'''
            <tr class="{estado_clase}">
              <td>{formatear_fecha(transaccion['fecha'])}</td>
              <td>{transaccion['tipo']}</td>
              <td>{transaccion['estado']}</td>
              <td>${transaccion['monto']:,}</td>
              <td>{transaccion.get('razon', '')}</td>
            </tr>'''
        
        html += '''
        </table>
        <hr>
        '''

    html += '''
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
