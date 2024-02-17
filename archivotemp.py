import pandas as pd
from docx import Document


# Abrir el documento Word existente
documento_word = Document('acta.docx')

# Cargar el archivo de Excel en un DataFrame con la cabecera en la fila 13 y comenzando desde la fila 14
df = pd.read_excel('Reporte de Juicios Evaluativos (1).xls',header=0,skiprows=12)


# Access the specific paragraph where you want to insert text
target_table = documento_word.tables[0]  # replace 0 with the index of the table
target_cell = target_table.cell(7, 1)  # Suponiendo que la celda está en la fila 7 y columna 1
target_paragraph = None


# Crear una nueva columna 'Nombre completo' concatenando 'Nombre' y 'Apellidos'
df['Nombrecompleto'] = df['Nombre'] + ' ' + df['Apellidos']


# informacion para la tabla de estudiantes 
dfestudiantes=df.loc[df['Estado'] == 'EN FORMACION', ['Nombrecompleto', 'Número de Documento','Estado']]
dfestudiantes = dfestudiantes.drop_duplicates(subset=['Nombrecompleto'])


# Buscar la frase dentro de la celda
for paragraph in target_cell.paragraphs:
    if "Lo cual indica que se encuentran" in paragraph.text:
    
    # Insertar la tabla debajo de la frase encontrada
        paragraph._p.addnext(tabla._element)
        break



"""# Crear un nuevo archivo Excel
with pd.ExcelWriter('informacion_estudiantes.xlsx') as writer:
    # Iterar sobre cada grupo de estudiantes
    for nombre_estudiante, datos_estudiante in grupos_estudiantes:
        # Guardar los datos del estudiante en una hoja separada
        datos_estudiante.to_excel(writer, sheet_name=nombre_estudiante, index=False)"""



documento_word.save('acta.docx')

print("exito")