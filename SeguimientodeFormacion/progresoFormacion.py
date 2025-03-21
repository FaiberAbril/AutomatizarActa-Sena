import pandas as pd
from openpyxl import load_workbook


# Cargar el archivo de Excel en un DataFrame con la cabecera en la fila 13 y comenzando desde la fila 14
df = pd.read_excel('Reporte de Instructores por Ficha.xls',header=0,skiprows=10)



#funcion de sumar las horas de competencia por horas programadas retorna lista 
def datos(df):
    # Verificar las primeras filas del DataFrame para asegurarnos de que se cargó correctamente
    print(df.head())

    # Sumar las horas programadas por competencia
    horas_por_competencia = df.groupby('Competencia')['Horas Programadas'].sum().reset_index()

    # Mostrar el resultado de la suma
    print(horas_por_competencia)
    return horas_por_competencia




dfdos = pd.read_excel('2849089_PROGRAMACION_2025 (2).xlsx',header=0,skiprows=1)
# Verificar las primeras filas del DataFrame para asegurarnos de que se cargó correctamente
print(dfdos.head())
