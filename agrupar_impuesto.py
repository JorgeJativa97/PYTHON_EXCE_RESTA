import pandas as pd

def procesar_excel(archivo_excel):
    # Leer el archivo Excel
    df = pd.read_excel("REPORTE_RECAUDADO_V3 .xls", engine="xlrd")

    
    # Asegurar que los nombres de las columnas sean correctos
    columnas_requeridas = ['COD', 'IMPUESTO', 'ANIO_EMISION', 'INTERES_RECAUDADO', 'VALOR_TOTAL_RECAUDADO']
    if not all(col in df.columns for col in columnas_requeridas):
        raise ValueError("El archivo Excel debe contener las columnas: 'Codigo_Impuesto', 'Impuesto', 'Anio', 'Interes_Recaudado', 'Valor_Recaudado'")
    
     # Agrupar por 'Codigo_Impuesto', 'Impuesto' y 'Anio' y sumar las columnas numéricas
    resultado = df.groupby(['COD', 'IMPUESTO', 'ANIO_EMISION'])[['INTERES_RECAUDADO', 'VALOR_TOTAL_RECAUDADO']].sum().reset_index()
    
    # Ordenar el resultado por 'Anio'
    resultado = resultado.sort_values(by='ANIO_EMISION')
    
    # Guardar el resultado en un nuevo archivo Excel
    resultado.to_excel("resultado.xlsx", index=False)
    print("Archivo procesado y guardado como 'resultado.xlsx'")
    
# Uso del script
# Cambia 'archivo.xlsx' por el nombre real de tu archivo
procesar_excel("archivo_final.xlsx")

#Explicación:

#Lectura del archivo: Usamos pd.read_excel() para cargar los datos.

#Agrupación: Utilizamos groupby() en las columnas 'cod' e 'impuesto'.

#Suma: Aplicamos .sum() solo a las columnas numéricas especificadas.

#Resultado: Obtenemos un nuevo DataFrame con la suma consolidada por código.
