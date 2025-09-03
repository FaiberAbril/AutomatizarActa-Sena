import pandas as pd

# Cargar el archivo de Excel principal
df_excel = pd.read_excel('2849089_PROGRAMACION_2025.xlsx', header=0, skiprows=1)

# Verificar las primeras filas del DataFrame para asegurarnos de que se cargó correctamente
print("DataFrame del archivo principal:")
print(df_excel.head())

# Cargar el archivo de Excel con las horas programadas
df = pd.read_excel('Reporte de Instructores por Ficha.xls', header=0, skiprows=10)

# Función para sumar las horas programadas por competencia
def sumar_horas_por_competencia(df):
    # Sumar las horas programadas por competencia
    horas_por_competencia = df.groupby('Competencia')['Horas Programadas'].sum().reset_index()
    return horas_por_competencia

# Obtener las horas programadas por competencia
horas_por_competencia = sumar_horas_por_competencia(df)

# Mostrar el resultado de la suma
print("\nHoras programadas por competencia:")
print(horas_por_competencia)

# Actualizar la columna "Ejecutadas" en el DataFrame del archivo de Excel
df_excel["Ejecutadas"] = df_excel["Competencias (NORMA / UNIDAD DE COMPETENCIA)"].map(
    horas_por_competencia.set_index("Competencia")["Horas Programadas"]
)

# Manejar valores nulos en la columna "Ejecutadas"
df_excel["Ejecutadas"] = df_excel["Ejecutadas"].fillna(0)  # Rellenar NaN con 0

# Calcular la columna "Por Ejecutar"
df_excel["Por Ejecutar"] = df_excel["Total"] - df_excel["Ejecutadas"]

# Guardar el archivo de Excel actualizado
df_excel.to_excel("archivo_actualizado.xlsx", index=False)

print("\nArchivo actualizado guardado como 'archivo_actualizado.xlsx'")
print("\nDataFrame actualizado:")
print(df_excel.head())