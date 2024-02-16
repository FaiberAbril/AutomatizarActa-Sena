import pandas as pd
from docx import Document


# Abrir el documento Word existente
documento_word = Document('acta.docx')

# Cargar el archivo de Excel en competencias
dfcompetencias = pd.read_excel('Reporte de Juicios Evaluativos (1).xls',header=0,skiprows=12)
dfcompetencias = dfcompetencias[dfcompetencias['Competencia'] != '2 - RESULTADOS DE APRENDIZAJE ETAPA PRACTICA']
grupos_competencia = dfcompetencias.groupby('Competencia')[['Competencia', 'Juicio de Evaluación']]
dfcompetencias['Juicio de Evaluación'] = dfcompetencias['Juicio de Evaluación'].apply(lambda x: 'Sí' if x == 'APROBADO' else 'No' if x == 'POR EVALUAR' else x)
dfcompetencias = dfcompetencias.drop_duplicates(subset=['Competencia'])






# Mostrar el DataFrame resultante
print(dfcompetencias[['Competencia', 'Juicio de Evaluación']])