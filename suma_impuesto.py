import pandas as pd

# Cargar el archivo Excel
df = pd.read_excel('impuesto.xlsx')

# Definir columnas numéricas a sumar (ajusta los nombres según tu archivo)
columnas_numericas = [
    'EMISION',
    'INTERES',
    'COACTIVA',
    'RECARGO',
    'DESCUENTO',
    'IVA',
    'TOTAL_RECAUDADO'
]

# Agrupar por código e impuesto, sumando todas las columnas numéricas
df_agrupado = df.groupby(['COD', 'IMPUESTO'], as_index=False)[columnas_numericas].sum()

# Mostrar resultado
print("\nResultado agrupado:")
print(df_agrupado)

# Guardar en nuevo archivo Excel (opcional)
df_agrupado.to_excel('impuestos_agrupados.xlsx', index=False)
print("\nArchivo guardado como 'impuestos_agrupados.xlsx'")