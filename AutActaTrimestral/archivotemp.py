import pandas as pd
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows


# Cargar el archivo de Excel en un DataFrame con la cabecera en la fila 13 y comenzando desde la fila 14
df = pd.read_excel('Reporte de Juicios Evaluativos.xls',header=0,skiprows=12)
# Crear una nueva columna 'Nombre completo' concatenando 'Nombre' y 'Apellidos'
df['Nombrecompleto'] = df['Nombre'] + ' ' + df['Apellidos']
dfcompetencias = df
dfcompetencias = dfcompetencias[dfcompetencias['Competencia'] != '2 - RESULTADOS DE APRENDIZAJE ETAPA PRACTICA']
dfcompetencias = dfcompetencias[dfcompetencias['Estado'] == 'EN FORMACION']
dfcompetencias['Juicio de Evaluación'] = dfcompetencias['Juicio de Evaluación'].apply(lambda x: 'Si' if x == 'APROBADO' else 'No' if x == 'POR EVALUAR' else x)
dfcompetencias = dfcompetencias[['Número de Documento','Nombrecompleto','Competencia','Juicio de Evaluación','Resultado de Aprendizaje']]
nombres_estudiantes = dfcompetencias['Nombrecompleto'].unique()





# Guardar los datos en un archivo Excel con una hoja por cada estudiante
with pd.ExcelWriter('competencias_evaluativas.xlsx', engine='openpyxl') as writer:
    for nombre_estudiante in nombres_estudiantes:
        # Filtrar los datos del estudiante actual
        datos_estudiante = dfcompetencias[dfcompetencias['Nombrecompleto'] == nombre_estudiante]


        total_juicio_evaluacionFormacion = datos_estudiante['Juicio de Evaluación'].count()


        aprobados = datos_estudiante[datos_estudiante['Juicio de Evaluación'] == 'Si']
        total_aprobados = aprobados['Juicio de Evaluación'].count()



        # Crear una hoja con el nombre del estudiante
        datos_estudiante.to_excel(writer, sheet_name=nombre_estudiante,startrow=5, index=False)

        # Obtener la hoja recién creada
        hoja_estudiante = writer.sheets[nombre_estudiante]
        # Agregar el nombre completo en la parte superior de la hoja
        hoja_estudiante['A1'] = "Nombre Completo Estudiante"
        hoja_estudiante['A2'] = nombre_estudiante


        hoja_estudiante['F1'] = "Total de Resultados de Aprendizaje"
        hoja_estudiante['F2'] = total_juicio_evaluacionFormacion


        hoja_estudiante['K1'] = "Total de Resultados de Aprobados"
        hoja_estudiante['K2'] = total_aprobados









# Leer el archivo Excel y mostrar los datos
df_excel = pd.read_excel('competencias_evaluativas.xlsx')
print("re creo correctamente")