import pandas as pd
from openpyxl import load_workbook


# Cargar el archivo de Excel en un DataFrame con la cabecera en la fila 13 y comenzando desde la fila 14
df = pd.read_excel('Reporte de Juicios Evaluativos (1).xls',header=0,skiprows=12)
# Crear una nueva columna 'Nombre completo' concatenando 'Nombre' y 'Apellidos'
df['Nombrecompleto'] = df['Nombre'] + ' ' + df['Apellidos']
dfcompetencias = df
dfcompetencias = dfcompetencias[dfcompetencias['Competencia'] != '2 - RESULTADOS DE APRENDIZAJE ETAPA PRACTICA']
dfcompetencias['Juicio de Evaluación'] = dfcompetencias['Juicio de Evaluación'].apply(lambda x: 'Si' if x == 'APROBADO' else 'No' if x == 'POR EVALUAR' else x)




dfcompetencias = dfcompetencias[['Número de Documento','Nombrecompleto','Competencia','Juicio de Evaluación','Resultado de Aprendizaje']]
nombres_estudiantes = dfcompetencias['Nombrecompleto'].unique()



dfcompetencias.to_excel('competencias_evaluativas.xlsx', index=False)

# Crear un archivo Excel con una hoja por cada estudiante
with pd.ExcelWriter('competencias_evaluativas.xlsx') as writer:
    for nombre_estudiante in nombres_estudiantes:
        # Filtrar los datos del estudiante actual
        datos_estudiante = dfcompetencias[dfcompetencias['Nombrecompleto'] == nombre_estudiante]
        # Guardar los datos del estudiante en una hoja
        datos_estudiante.to_excel(writer, sheet_name=nombre_estudiante, index=False)





print(dfcompetencias)