import pandas as pd
from docx import Document


# Abrir el documento Word existente
documento_word = Document('acta.docx')

# Cargar el archivo de Excel en competencias
dfcompetenciassinevaluar = pd.read_excel('Reporte de Juicios Evaluativos (1).xls',header=0,skiprows=12)
dfcompetenciassinevaluar = dfcompetenciassinevaluar[['Competencia','Resultado de Aprendizaje','Juicio de Evaluación']]
dfcompetenciassinevaluar = dfcompetenciassinevaluar[dfcompetenciassinevaluar['Competencia'] != '2 - RESULTADOS DE APRENDIZAJE ETAPA PRACTICA']
dfcompetenciassinevaluar['Juicio de Evaluación'] = dfcompetenciassinevaluar['Juicio de Evaluación'].apply(lambda x: 'Si' if x == 'APROBADO' else 'No' if x == 'POR EVALUAR' else x)



# Supongamos que dfcompetenciassinevaluar es tu DataFrame original
dfcompetenciassinevaluar = dfcompetenciassinevaluar.groupby('Resultado de Aprendizaje').agg({'Juicio de Evaluación': lambda x: (x == 'Si').sum(), 'Competencia': 'first'}).reset_index()

# Ahora, si deseas filtrar las filas donde el conteo de 'Sí' es igual a cero y obtener las columnas 'Competencia' y 'Resultado de Aprendizaje':
dfcompetenciassinevaluar = dfcompetenciassinevaluar[dfcompetenciassinevaluar['Juicio de Evaluación'] == 0][['Competencia', 'Resultado de Aprendizaje']]

dfcompetenciassinevaluar  = dfcompetenciassinevaluar[['Competencia','Resultado de Aprendizaje']]


print(dfcompetenciassinevaluar)



"""

dfcompetenciassinevaluar = dfcompetenciassinevaluar[dfcompetenciassinevaluar['Juicio de Evaluación'] == 'No']
dfcompetenciassinevaluar['Juicio de Evaluación'] = dfcompetenciassinevaluar.apply(lambda row: 'Sí' if not pd.isnull(row['Resultado de Aprendizaje']) else 'No', axis=1)


conteo_si = dfcompetenciassinevaluar.groupby('Resultado de Aprendizaje')['Juicio de Evaluación'].apply(lambda x: (x == 'Si').sum()).reset_index()
conteo_no = dfcompetenciassinevaluar.groupby('Resultado de Aprendizaje')['Juicio de Evaluación'].apply(lambda x: (x == 'No').sum()).reset_index()

documentos_con_mas_de_un_no = ['Competencia'] & conteo_no[conteo_no['Juicio de Evaluación'] == 0 ]['Resultado de Aprendizaje']



documentos_con_mas_de_un_si = conteo_si[conteo_si['Juicio de Evaluación'] > 1]['Resultado de Aprendizaje']

dfcompetenciassinevaluar = dfcompetenciassinevaluar.apply(lambda row: 'No' if row['Resultado de Aprendizaje'] in documentos_con_mas_de_un_si else row['Juicio de Evaluación'], axis=1)




# Mostrar el DataFrame resultante
#print(dfcompetencias[['Competencia', 'Juicio de Evaluación']])"""


