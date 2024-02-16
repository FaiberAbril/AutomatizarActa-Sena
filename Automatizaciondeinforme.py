import pandas as pd
from docx import Document


# Abrir el documento Word existente
documento_word = Document('acta.docx')

# Cargar el archivo de Excel en un DataFrame con la cabecera en la fila 13 y comenzando desde la fila 14
df = pd.read_excel('Reporte de Juicios Evaluativos (1).xls',header=0,skiprows=12)



# Crear una nueva columna 'Nombre completo' concatenando 'Nombre' y 'Apellidos'
df['Nombrecompleto'] = df['Nombre'] + ' ' + df['Apellidos']


# informacion para la tabla de estudiantes 

dfestudiantes=df.loc[df['Estado'] == 'EN FORMACION', ['Nombrecompleto', 'Número de Documento','Estado']]
dfestudiantes = dfestudiantes.drop_duplicates(subset=['Nombrecompleto'])


# Agregar una tabla al final del documento
tabla = documento_word.add_table(rows=len(dfestudiantes) + 1, cols=3)  # +1 para incluir el encabezado
tabla.style = 'Table Grid'  # Aplicar un estilo de tabla

# Agregar el encabezado de la tabla
encabezado = tabla.rows[0].cells
encabezado[0].text = 'Nombre Completo'
encabezado[1].text = 'Número de Documento'
encabezado[2].text = 'Estado'

# Agregar los datos de las columnas especificadas a la tabla
for i, (_, fila) in enumerate(dfestudiantes.iterrows(), start=1):
    celdas = tabla.rows[i].cells
    celdas[0].text = fila['Nombrecompleto']
    celdas[1].text = str(fila['Número de Documento'])  # Convertir a cadena si no es texto
    celdas[2].text = fila['Estado']


# Agregar un párrafo en blanco entre las tablas
documento_word.add_paragraph()



# informacion para la tabla de estudiantes por retiros 
dfestudiantes=df.loc[df['Estado'] != 'EN FORMACION', ['Nombrecompleto', 'Número de Documento','Estado']]
dfestudiantesretiro = dfestudiantes.drop_duplicates(subset=['Nombrecompleto'])


# Agregar una tabla al final del documento
tablaRetiro = documento_word.add_table(rows=len(dfestudiantesretiro) + 1, cols=3)  # +1 para incluir el encabezado
tablaRetiro.style = 'Table Grid'  # Aplicar un estilo de tabla

# Agregar el encabezado de la tabla
encabezado = tablaRetiro.rows[0].cells
encabezado[0].text = 'Nombre Completo'
encabezado[1].text = 'Número de Documento'
encabezado[2].text = 'Estado'

# Agregar los datos de las columnas especificadas a la tabla
for i, (_, fila) in enumerate(dfestudiantesretiro.iterrows(), start=1):
    celdas = tablaRetiro.rows[i].cells
    celdas[0].text = fila['Nombrecompleto']
    celdas[1].text = str(fila['Número de Documento'])  # Convertir a cadena si no es texto
    celdas[2].text = fila['Estado']



# Agregar un párrafo en blanco entre las tablas
documento_word.add_paragraph()


# Cargar el archivo de Excel en competencias
dfcompetencias = df
dfcompetencias = dfcompetencias[dfcompetencias['Competencia'] != '2 - RESULTADOS DE APRENDIZAJE ETAPA PRACTICA']
grupos_competencia = dfcompetencias.groupby('Competencia')[['Competencia', 'Juicio de Evaluación']]
dfcompetencias['Juicio de Evaluación'] = dfcompetencias['Juicio de Evaluación'].apply(lambda x: 'Si' if x == 'APROBADO' else 'No' if x == 'POR EVALUAR' else x)
dfcompetencias = dfcompetencias.drop_duplicates(subset=['Competencia'])




# Agregar una tabla al final del documento
tablaCompetencias = documento_word.add_table(rows=len(dfcompetencias) + 1, cols=2)  # +1 para incluir el encabezado
tablaCompetencias.style = 'Table Grid'  # Aplicar un estilo de tabla

# Agregar el encabezado de la tabla
encabezado = tablaCompetencias.rows[0].cells
encabezado[0].text = 'Competencias Desarrolladas'
encabezado[1].text = 'Evaluado En SOFIAPLUS'


# Agregar los datos de las columnas especificadas a la tabla
for i, (_, fila) in enumerate(dfcompetencias.iterrows(), start=1):
    celdas = tablaCompetencias.rows[i].cells
    celdas[0].text = fila['Competencia']
    celdas[1].text = str(fila['Juicio de Evaluación'])  # Convertir a cadena si no es texto




# Agregar un párrafo en blanco entre las tablas
documento_word.add_paragraph()

# resultados y competencias sin evaluar
dfcompetenciassinevaluar = df
dfcompetenciassinevaluar = dfcompetenciassinevaluar[['Competencia','Resultado de Aprendizaje','Juicio de Evaluación']]
dfcompetenciassinevaluar = dfcompetenciassinevaluar[dfcompetenciassinevaluar['Competencia'] != '2 - RESULTADOS DE APRENDIZAJE ETAPA PRACTICA']
dfcompetenciassinevaluar['Juicio de Evaluación'] = dfcompetenciassinevaluar['Juicio de Evaluación'].apply(lambda x: 'Si' if x == 'APROBADO' else 'No' if x == 'POR EVALUAR' else x)


# Supongamos que dfcompetenciassinevaluar es tu DataFrame original
dfcompetenciassinevaluar = dfcompetenciassinevaluar.groupby('Resultado de Aprendizaje').agg({'Juicio de Evaluación': lambda x: (x == 'Si').sum(), 'Competencia': 'first'}).reset_index()

# Ahora, si deseas filtrar las filas donde el conteo de 'Sí' es igual a cero y obtener las columnas 'Competencia' y 'Resultado de Aprendizaje':
dfcompetenciassinevaluar = dfcompetenciassinevaluar[dfcompetenciassinevaluar['Juicio de Evaluación'] == 0][['Competencia', 'Resultado de Aprendizaje']]
# Obtener los datos de las competencias y los resultados de aprendizaje
dfcompetenciassinevaluar = dfcompetenciassinevaluar[['Competencia', 'Resultado de Aprendizaje']]

# Agregar una tabla al final del documento
tablaCompetenciassinevaluar = documento_word.add_table(rows=len(dfcompetenciassinevaluar) + 1, cols=2)  # +1 para incluir el encabezado
tablaCompetenciassinevaluar.style = 'Table Grid'  # Aplicar un estilo de tabla

# Agregar el encabezado de la tabla
encabezado = tablaCompetenciassinevaluar.rows[0].cells
encabezado[0].text = 'Competencia'
encabezado[1].text = 'Resultado de Aprendizaje sin Evaluar'

# Iterar sobre las filas de la tabla y los datos del DataFrame
for i, (index, fila) in enumerate(dfcompetenciassinevaluar.iterrows(), start=1):
    # Acceder a las celdas de la fila
    celdas = tablaCompetenciassinevaluar.rows[i].cells
    # Asignar los datos a las celdas
    celdas[0].text = str(fila['Competencia'])
    celdas[1].text = str(fila['Resultado de Aprendizaje'])



# Agregar un párrafo en blanco entre las tablas
documento_word.add_paragraph()



documento_word.save('acta.docx')

print("Se ha agregado una tabla al final del documento de Word con los datos de las columnas especificadas.")