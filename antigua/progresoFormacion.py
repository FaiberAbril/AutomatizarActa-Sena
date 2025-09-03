import pandas as pd

# Cargar el archivo de Excel principal
df_excel = pd.read_excel('2849089_PROGRAMACION_2025.xlsx', header=0, skiprows=1)

# Cargar el archivo de Excel con las horas programadas
df = pd.read_excel('Reporte de Instructores por Ficha.xls', header=0, skiprows=10)



# Función para sumar las horas programadas por competencia
def sumar_horas_por_competencia(df):
    # Sumar las horas programadas por competencia
    horas_por_competencia = df.groupby('Competencia', as_index=False)['Horas Programadas'].sum()
    return horas_por_competencia




# Obtener las horas programadas por competencia
horas_por_competencia = sumar_horas_por_competencia(df)

# Mostrar el resultado de la suma
#print("\nHoras programadas por competencia:")
#print(horas_por_competencia)


def sumar_horas_por_competencia_totales(df):
    # Sumar todos los valores de la columna 'Total'
    suma_total = df['Total '].sum()
    return suma_total

print(sumar_horas_por_competencia_totales(df_excel))


def sumar_horas_por_competencia_ejecutadas(df):
    # Sumar todos los valores de la columna 'Total'
    suma_total = df['Ejecutadas'].sum()
    return suma_total

print(sumar_horas_por_competencia_ejecutadas(df_excel))


def sumar_horas_por_competencia_ejecutadas(df):
    # Sumar todos los valores de la columna 'Total'
    suma_total = df['Ejecutadas'].sum()
    return suma_total

print(sumar_horas_por_competencia_ejecutadas(df_excel))