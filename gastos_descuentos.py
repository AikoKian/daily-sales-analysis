# Según la info de ventas registradas por un supermercado a lo largo de un día
# averiguar cuál fue el número vendido de cada uno de los productos.
# qué clientes gastaron más de 50 pesos y ofrecerles un descuento la proxima.
# cuánto gasta un cliente en promedio en un día en el local.
import pandas as pd
import matplotlib.pyplot as plt
import urllib.request as ur

# URL del archivo hoja de calculo excel
url = "https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/datosClientes.xlsx"

# Descargar y guardar el archivo
try:
    ur.urlretrieve(url, "datosClientes.xlsx")
    print("Archivo descargado exitosamente como 'datosClientes.xlsx'")
except Exception as e:
    print(f"Ocurrió un error: {str(e)}")


# leer el archivo excel
try:
    datos = pd.read_excel("datosClientes.xlsx")
    print("Archivo leído exitosamente")
except Exception as e:
    print(f"Ocurrio un erro al leer el archivo {str(e)}")
    
# print(datos)

# 1. num. vendido de cada producto en el día
try:
    productos_vendidos = datos.groupby('Producto comprado')['Numero comprado'].sum()
    print(f"\n1. Numero vendido de cada producto:")
    print(productos_vendidos)
    
    # Gráfico de barras
    plt.figure(figsize=(8,5))
    productos_vendidos.sort_values(ascending=False).plot(kind='bar', color="skyblue", edgecolor="black")
    plt.title("Número de productos vendidos en el día")
    plt.xlabel("Producto")
    plt.ylabel("Cantidad vendida")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()
except Exception as e:
    print(f"Ocurrio un erro al calcular: {str(e)}")

# 2. clientes que gastaron mas de 50 pesos
try:
    # Calcular el gasto x compra
    datos['Gasto'] = datos['Numero comprado'] * datos['Valor del producto']
    # Sumar el gasto por cliente
    gasto_x_cliente = datos.groupby('Nombre')['Gasto'].sum()
    # Filtrar clientes que gastaron mas de 50 pesos
    clientes_descuento = gasto_x_cliente[gasto_x_cliente > 50]
    print(f"\n2. Clientes que gastaron mas de 50 pesos (elegibles para descuentos):")
    print(clientes_descuento)
except Exception as e:
    print(f"Ocurrio un erro al calcular: {str(e)}")
    
# 3. Promedio de gasto por cliente
try:
    promedio_gasto = gasto_x_cliente.mean()
    print(f"\n3. Gasto promedio por cliente: ${promedio_gasto:.2f}")
except Exception as e:
    print(f"Error al calcular promedio de gasto: {str(e)}")
