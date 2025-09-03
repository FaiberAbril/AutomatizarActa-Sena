import pandas as pd
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows
import re


# Cargar el archivo de Excel en un DataFrame con la cabecera en la fila 13 y comenzando desde la fila 14
df = pd.read_excel('Reporte de Juicios Evaluativos.xls',header=0,skiprows=12)

# Cargar el archivo de Excel en un DataFrame con la cabecera en la fila 13 y comenzando desde la fila 14
dfreporte = pd.read_excel('Reporte de Instructores por Ficha.xls',header=0,skiprows=10)
dfreporte = dfreporte['Competencia'].unique()



# Crear una nueva columna 'Nombre completo'
df['Nombrecompleto'] = df['Nombre'] + ' ' + df['Apellidos']



# Definir una función para eliminar números y guiones de las competencias
def limpiar_competencia(texto):
    # Usa una expresión regular para eliminar números y guiones
    return re.sub(r'^\d+\s*-\s*', '', texto).strip()

# Aplicar la función a la columna 'Competencia'
df['Competencia'] = df['Competencia'].apply(limpiar_competencia)


# Agregar una nueva columna en df1 para indicar si la competencia está en df2
df['Vista'] = df['Competencia'].apply(lambda x: 'Vista' if x in dfreporte else 'NO')


# Filtrar los datos
dfcompetencias = df[
    (df['Competencia'] != '2 - RESULTADOS DE APRENDIZAJE ETAPA PRACTICA') &
    (df['Estado'] == 'EN FORMACION')
]

# Reemplazar valores en 'Juicio de Evaluación'
dfcompetencias.loc[:, 'Juicio de Evaluación'] = dfcompetencias['Juicio de Evaluación'].replace({
    'POR EVALUAR': 'No'
})

# Obtener la lista de nombres de estudiantes únicos
nombres_estudiantes = dfcompetencias['Nombrecompleto'].unique()

# Seleccionar las columnas relevantes
dfcompetencias = dfcompetencias[[ 'Nombrecompleto','Vista', 'Competencia', 'Juicio de Evaluación', 'Resultado de Aprendizaje']]


# Guardar los datos en un archivo Excel con una hoja por cada estudiante
with pd.ExcelWriter('competencias_evaluativas.xlsx', engine='openpyxl') as writer:
    for nombre_estudiante in nombres_estudiantes:
        # Filtrar los datos del estudiante actual
        datos_estudiante = dfcompetencias[dfcompetencias['Nombrecompleto'] == nombre_estudiante]
        total_juicio_evaluacionFormacion = datos_estudiante['Juicio de Evaluación'].count()
        aprobados = datos_estudiante[datos_estudiante['Juicio de Evaluación'] == 'APROBADO']
        total_aprobados = aprobados['Juicio de Evaluación'].count()



        # Crear una hoja con el nombre del estudiante
        datos_estudiante.to_excel(writer, sheet_name=nombre_estudiante,startrow=5, index=False)

        # Obtener la hoja recién creada
        hoja_estudiante = writer.sheets[nombre_estudiante]
        # Agregar el nombre completo en la parte superior de la hoja
        hoja_estudiante['A1'] = "Nombre Completo Estudiante"
        hoja_estudiante['A2'] = nombre_estudiante
        hoja_estudiante['F1'] = "Total de Resultados de Aprobados"
        hoja_estudiante['F2'] = total_aprobados
        hoja_estudiante['K1'] = "Total de Resultados de Aprendizaje"
        hoja_estudiante['K2'] = total_juicio_evaluacionFormacion




# Seleccionar las columnas relevantes
dfcompetencias = dfcompetencias[['Competencia', 'Juicio de Evaluación', 'Resultado de Aprendizaje']]




# Leer el archivo Excel y mostrar los datos
df_excel = pd.read_excel('competencias_evaluativas.xlsx')
print("re creo correctamente")