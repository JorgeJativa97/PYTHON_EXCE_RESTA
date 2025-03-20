import pandas as pd

# Cargar los archivos .xls
df1 = pd.read_excel("CARTERA VENCIDA.xls", engine='xlrd')  # Usar engine='xlrd' para .xls
df2 = pd.read_excel("R-total_a.xls", engine='xlrd')

# 1. Filtrar y sumar Tasa de Alcantarillado (códigos 1 y 28) por año en df1
# --------------------------------------------------------------------------
# Crear una máscara para filtrar el impuesto y los códigos


# Combinar ambos DataFrames por 'impuesto' y 'año'
merged_df = pd.merge(
    df1,
    df2,
    on=["COD","IMPUESTO", "ANIO"],
    how="left",  
    suffixes=('_CARTERA VENCIDA', '_R-total_a')
)

# Rellenar NaN (valores faltantes) con 0 en 'valor_archivo2'
merged_df["VALOR_TOTAL_RECAUDADO"] = merged_df["VALOR_TOTAL_RECAUDADO"].fillna(0)
merged_df["INTERES_RECAUDADO"] = merged_df["INTERES_RECAUDADO"].fillna(0)

# Calcular la diferencia
merged_df["diferencia"] = merged_df["TOTAL_RECAUDADO"] - merged_df["VALOR_TOTAL_RECAUDADO"]
merged_df["diferencia_interes"] = merged_df["INTERES"] - merged_df["INTERES_RECAUDADO"]

# Seleccionar columnas relevantes
#resultado = merged_df[["IMPUESTO", "ANIO", "TOTAL_RECAUDADO", "TOTAL", "diferencia"]]

columnas_finales = df1.columns.tolist() + ["diferencia", "diferencia_interes"]
resultado = merged_df[columnas_finales]

# Guardar el resultado en un nuevo archivo (puede ser .xlsx o .xls)
resultado.to_excel("resultado_diferencias.xlsx", index=False, engine='openpyxl')  # Usamos .xlsx para el resultado

print("¡Listo! Revisa el archivo 'resultado_diferencias.xlsx'")