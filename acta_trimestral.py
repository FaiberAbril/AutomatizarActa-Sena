import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import os
import shutil
from docx import Document


# Función para seleccionar y copiar el archivo al proyecto
def seleccionar_y_copiar_archivo():
    # Abrir un diálogo para seleccionar el archivo desde el sistema operativo
    archivo_origen = filedialog.askopenfilename(
        title="Seleccionar archivo de Excel",
        filetypes=[("Excel files", "*.xls *.xlsx")]
    )

    if archivo_origen:  # Si el usuario seleccionó un archivo
        try:
            # Obtener la ruta del directorio actual (carpeta del proyecto)
            directorio_actual = os.getcwd()
            # Obtener el nombre del archivo seleccionado
            nombre_fijo = "Reporte de Juicios Evaluativos.xls"
            # Ruta de destino (carpeta del proyecto + nombre del archivo)
            ruta_destino = os.path.join(directorio_actual, nombre_fijo)

            # Copiar el archivo seleccionado a la carpeta del proyecto
            shutil.copy(archivo_origen, ruta_destino)

            # Mostrar mensaje de éxito
            messagebox.showinfo("Éxito", f"Archivo copiado a: {ruta_destino}")

            # Cargar el archivo copiado
            cargar_archivo(ruta_destino)  # Pasar la ruta del archivo como argumento
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo copiar el archivo: {e}")


def seleccionar_y_copiar_archivoinstructor():
    # Abrir un diálogo para seleccionar el archivo desde el sistema operativo
    archivo_origen = filedialog.askopenfilename(
        title="Seleccionar archivo de Excel",
        filetypes=[("Excel files", "*.xls *.xlsx")]
    )

    if archivo_origen:  # Si el usuario seleccionó un archivo
        try:
            # Obtener la ruta del directorio actual (carpeta del proyecto)
            directorio_actual = os.getcwd()
            # Obtener el nombre del archivo seleccionado
            nombre_fijo = "Reporteporinstructor.xls"
            # Ruta de destino (carpeta del proyecto + nombre del archivo)
            ruta_destino = os.path.join(directorio_actual, nombre_fijo)

            # Copiar el archivo seleccionado a la carpeta del proyecto
            shutil.copy(archivo_origen, ruta_destino)

            # Mostrar mensaje de éxito
            messagebox.showinfo("Éxito", f"Archivo copiado a: {ruta_destino}")

            # Cargar el archivo copiado
            cargar_archivo(ruta_destino)  # Pasar la ruta del archivo como argumento
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo copiar el archivo: {e}")


# Función para cargar el archivo de Excel
def cargar_archivo(ruta_archivo):
    if os.path.exists(ruta_archivo):  # Verificar si el archivo existe
        try:
            # Cargar el archivo de Excel en un DataFrame
            df = pd.read_excel(ruta_archivo, header=0, skiprows=12)
            
            # Mostrar el DataFrame en una ventana de mensaje
            messagebox.showinfo("Datos Cargados", str(df.head()))
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar el archivo: {e}")
    else:
        messagebox.showerror("Error", f"El archivo no se encontró en la ruta: {ruta_archivo}")




# Función para abrir la ventana de Acta Trimestral
def abrir_ventana_acta_trimestral():
    # Crear una nueva ventana (Toplevel)
    ventana_acta_trimestral = tk.Toplevel()
    ventana_acta_trimestral.title("Cargar ")  # Título de la ventana
    ventana_acta_trimestral.geometry("600x600")  # Tamaño de la ventana

    # Agregar contenido a la ventana de Acta Trimestral
    etiqueta = tk.Label(ventana_acta_trimestral, text="Seleccione el archivo de Excel para cargar")
    etiqueta.pack(pady=20)

    # Crear un botón para seleccionar y copiar el archivo
    boton_seleccionar = tk.Button(ventana_acta_trimestral, text="Seleccionar Reporte de Juicios Evaluativos", command=seleccionar_y_copiar_archivo)
    boton_seleccionar.pack(pady=20)

    # Agregar contenido a la ventana de Acta Trimestral
    etiqueta = tk.Label(ventana_acta_trimestral, text="Seleccione el archivo de Excel para cargar")
    etiqueta.pack(pady=20)

    # Crear un botón para seleccionar y copiar el archivo
    boton_seleccionar = tk.Button(ventana_acta_trimestral, text="Seleccionar Reporte de horas por instructor", command=seleccionar_y_copiar_archivoinstructor)
    boton_seleccionar.pack(pady=20)


    # Agregar contenido a la ventana de Acta Trimestral
    etiqueta = tk.Label(ventana_acta_trimestral, text="GENERACION DE ACTA")
    etiqueta.pack(pady=20)

    # Crear un botón para seleccionar y copiar el archivo
    boton_seleccionar = tk.Button(ventana_acta_trimestral, text="GENERAR", command=generaracta)
    boton_seleccionar.pack(pady=20)



    # Crear un botón para cerrar la ventana
    boton_cerrar = tk.Button(ventana_acta_trimestral, text="Cerrar", command=ventana_acta_trimestral.destroy)
    boton_cerrar.pack(pady=10)





def generaracta():
    try:
        # Ruta del archivo original
        ruta_original = 'acta.docx'

        # Nombre del archivo copiado
        nombre_copia = 'actagenerada.docx'

        # Obtener la carpeta donde está el archivo original
        carpeta = os.path.dirname(ruta_original)

        # Crear la ruta completa de destino (misma carpeta, nombre diferente)
        ruta_destino = os.path.join(carpeta, nombre_copia)

        # Copiar el archivo a la misma carpeta con el nuevo nombre
        shutil.copy(ruta_original, ruta_destino)

        print(f"El archivo se ha copiado y renombrado correctamente en: {ruta_destino}")

        # Abrir el documento Word existente
        documento_word = Document(ruta_destino)

        # Cargar el archivo de Excel en un DataFrame con la cabecera en la fila 13 y comenzando desde la fila 14
        df = pd.read_excel('Reporte de Juicios Evaluativos.xls', header=0, skiprows=12)

        # Cargar el archivo de Excel en competencias
        dfinstructorhoras = pd.read_excel('Reporteporinstructor.xls', header=0, skiprows=10)

        # Access the specific paragraph where you want to insert text
        target_table = documento_word.tables[0]  # replace 0 with the index of the table
        target_cell = target_table.cell(7, 1)  # Suponiendo que la celda está en la fila 7 y columna 1

        # Crear una nueva columna 'Nombre completo' concatenando 'Nombre' y 'Apellidos'
        df['Nombrecompleto'] = df['Nombre'] + ' ' + df['Apellidos']

        # Información para la tabla de estudiantes
        dfestudiantes = df.loc[df['Estado'] == 'EN FORMACION', ['Nombrecompleto', 'Número de Documento', 'Estado']]
        dfestudiantes = dfestudiantes.drop_duplicates(subset=['Nombrecompleto'])

        # Buscar la frase dentro de la celda
        for paragraph in target_cell.paragraphs:
            if "Lo cual indica que se encuentran" in paragraph.text:
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

                # Insertar la tabla debajo de la frase encontrada
                paragraph._p.addnext(tabla._element)
                break

        # Agregar un párrafo en blanco entre las tablas
        documento_word.add_paragraph()

        # Información para la tabla de estudiantes por retiros
        dfestudiantesretiro = df.loc[df['Estado'] != 'EN FORMACION', ['Nombrecompleto', 'Número de Documento', 'Estado']]
        dfestudiantesretiro = dfestudiantesretiro.drop_duplicates(subset=['Nombrecompleto'])

        # Buscar la frase dentro de la celda
        for paragraph in target_cell.paragraphs:
            if "tabla de los cancelados y novedades de retiro se puede eliminar de la tabla anterior" in paragraph.text:
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

                # Insertar la tabla debajo de la frase encontrada
                paragraph._p.addnext(tablaRetiro._element)
                break

        # Agregar un párrafo en blanco entre las tablas
        documento_word.add_paragraph()

        # Cargar el archivo de Excel en competencias
        dfcompetencias = df
        dfcompetencias = dfcompetencias[dfcompetencias['Competencia'] != '2 - RESULTADOS DE APRENDIZAJE ETAPA PRACTICA']
        dfcompetencias['Juicio de Evaluación'] = dfcompetencias['Juicio de Evaluación'].apply(
            lambda x: 'Si' if x == 'APROBADO' else 'No' if x == 'POR EVALUAR' else x)
        dfcompetencias = dfcompetencias.drop_duplicates(subset=['Competencia'])

        # Buscar la frase dentro de la celda
        for paragraph in target_cell.paragraphs:
            if "3.2.1 Competencias Evaluadas" in paragraph.text:
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

                # Insertar la tabla debajo de la frase encontrada
                paragraph._p.addnext(tablaCompetencias._element)
                break

        # Agregar un párrafo en blanco entre las tablas
        documento_word.add_paragraph()

        # Resultados y competencias sin evaluar
        dfcompetenciassinevaluar = df
        dfcompetenciassinevaluar = dfcompetenciassinevaluar[['Competencia', 'Resultado de Aprendizaje', 'Juicio de Evaluación']]
        dfcompetenciassinevaluar = dfcompetenciassinevaluar[
            dfcompetenciassinevaluar['Competencia'] != '2 - RESULTADOS DE APRENDIZAJE ETAPA PRACTICA']
        dfcompetenciassinevaluar['Juicio de Evaluación'] = dfcompetenciassinevaluar['Juicio de Evaluación'].apply(
            lambda x: 'Si' if x == 'APROBADO' else 'No' if x == 'POR EVALUAR' else x)

        # Filtrar las filas donde el conteo de 'Sí' es igual a cero y obtener las columnas 'Competencia' y 'Resultado de Aprendizaje'
        dfcompetenciassinevaluar = dfcompetenciassinevaluar.groupby('Resultado de Aprendizaje').agg(
            {'Juicio de Evaluación': lambda x: (x == 'Si').sum(), 'Competencia': 'first'}).reset_index()
        dfcompetenciassinevaluar = dfcompetenciassinevaluar[dfcompetenciassinevaluar['Juicio de Evaluación'] == 0][
            ['Competencia', 'Resultado de Aprendizaje']]

        # Buscar la frase dentro de la celda
        for paragraph in target_cell.paragraphs:
            if "3.2.2 Competencias y Resultados de Aprendizaje por Evaluar" in paragraph.text:
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

                # Insertar la tabla debajo de la frase encontrada
                paragraph._p.addnext(tablaCompetenciassinevaluar._element)
                break

        # Agregar un párrafo en blanco entre las tablas
        documento_word.add_paragraph()

        # Horas de planeación
        horas_planeacion = {
            'Utilizar herramientas informáticas de acuerdo con las necesidades de manejo de información': 48,
            'APLICAR PRÁCTICAS DE PROTECCIÓN AMBIENTAL, SEGURIDAD Y SALUD EN EL TRABAJO DE ACUERDO CON LAS POLÍTICAS ORGANIZACIONALES Y LA NORMATIVIDAD VIGENTE.': 48,
            'Razonar cuantitativamente frente a situaciones susceptibles de ser abordadas de manera matemática en contextos laborales, sociales y personales.': 48,
            'APLICACIÓN DE CONOCIMIENTOS DE LAS CIENCIAS NATURALES DE ACUERDO CON SITUACIONES DEL CONTEXTO PRODUCTIVO Y SOCIAL.': 48,
            'DESARROLLAR PROCESOS DE COMUNICACIÓN EFICACES Y EFECTIVOS, TENIENDO EN CUENTA SITUACIONES  DE ORDEN SOCIAL, PERSONAL Y PRODUCTIVO.': 48,
            'GENERAR HÁBITOS SALUDABLES DE VIDA MEDIANTE LA APLICACIÓN DE PROGRAMAS DE ACTIVIDAD FÍSICA EN LOS CONTEXTOS PRODUCTIVOS Y SOCIALES.': 48,
            'Orientar investigación formativa según referentes técnicos': 48,
            'Enrique Low Murtra-Interactuar en el contexto productivo y social de acuerdo con principios  éticos para la construcción de una cultura de paz.': 48,
            'INTERACTUAR EN LENGUA INGLESA DE FORMA ORAL Y ESCRITA DENTRO DE CONTEXTOS SOCIALES Y LABORALES SEGÚN LOS CRITERIOS ESTABLECIDOS POR EL MARCO COMÚN EUROPEO DE REFERENCIA PARA LAS LENGUAS.': 384,
            'Fomentar cultura emprendedora según habilidades y competencias personales': 48
        }

        dfinstructorhoras['Nombrecompleto'] = dfinstructorhoras['Nombre Instructor'] + ' ' + dfinstructorhoras['Apellido Instructor']
        dfinstructorhoras = dfinstructorhoras.sort_values(by='Competencia', ascending=True)

        # Añadir la columna 'Horas Planeadas' al DataFrame
        dfinstructorhoras['Horas Planeadas'] = dfinstructorhoras['Competencia'].map(horas_planeacion)

        dfinstructorhoras = dfinstructorhoras[['Nombrecompleto', 'Estado Instructor', 'Competencia', 'Horas Programadas', 'Horas Planeadas']]

        # Buscar la frase dentro de la celda
        for paragraph in target_cell.paragraphs:
            if "El reporte de instructor por ficha en SOFIA PLUS es:" in paragraph.text:
                # Agregar una tabla al final del documento
                tablainstructores = documento_word.add_table(rows=len(dfinstructorhoras) + 1, cols=5)  # +1 para incluir el encabezado
                tablainstructores.style = 'Table Grid'  # Aplicar un estilo de tabla

                # Agregar el encabezado de la tabla
                encabezado = tablainstructores.rows[0].cells
                encabezado[0].text = 'Nombre completo Instructor'
                encabezado[1].text = 'Estado Instructor'
                encabezado[2].text = 'Competencia'
                encabezado[3].text = 'Horas Programadas en sofia plus'
                encabezado[4].text = 'Horas Planeacion'

                # Iterar sobre las filas de la tabla y los datos del DataFrame
                for i, (index, fila) in enumerate(dfinstructorhoras.iterrows(), start=1):
                    # Acceder a las celdas de la fila
                    celdas = tablainstructores.rows[i].cells
                    # Asignar los datos a las celdas
                    celdas[0].text = str(fila['Nombrecompleto'])
                    celdas[1].text = str(fila['Estado Instructor'])
                    celdas[2].text = str(fila['Competencia'])
                    celdas[3].text = str(fila['Horas Programadas'])
                    celdas[4].text = str(fila['Horas Planeadas'])

                # Insertar la tabla debajo de la frase encontrada
                paragraph._p.addnext(tablainstructores._element)
                break

        # Agregar un párrafo en blanco entre las tablas
        documento_word.add_paragraph()

        # Guardar el documento generado
        documento_word.save(ruta_destino)
        messagebox.showinfo("Éxito", "El archivo se generó correctamente.")

        # Llamar a la función para guardar el documento en la ubicación deseada
        guardar_documento(ruta_destino)

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al generar el acta: {e}")


def guardar_documento(ruta_archivo):
    # Abrir un cuadro de diálogo para que el usuario elija la ubicación y el nombre del archivo
    ruta_guardado = filedialog.asksaveasfilename(
        defaultextension=".docx",
        filetypes=[("Documentos Word", "*.docx"), ("Todos los archivos", "*.*")],
        title="Guardar archivo como",
        initialfile="actagenerada.docx"  # Nombre sugerido para el archivo
    )

    # Si el usuario selecciona una ubicación (no cancela el diálogo)
    if ruta_guardado:
        try:
            # Copiar el archivo generado a la ubicación seleccionada
            shutil.copy(ruta_archivo, ruta_guardado)
            messagebox.showinfo("Éxito", f"El archivo se guardó correctamente en:\n{ruta_guardado}")

            # Eliminar los archivos temporales
            archivos_a_eliminar = [
                'actagenerada.docx',
                'Reporte de Juicios Evaluativos.xls',
                'Reporteporinstructor.xls'
            ]

            for archivo in archivos_a_eliminar:
                if os.path.exists(archivo):
                    os.remove(archivo)
                    print(f"Archivo eliminado: {archivo}")
                else:
                    print(f"El archivo no existe: {archivo}")

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar o eliminar los archivos: {e}")
    else:
        messagebox.showwarning("Cancelado", "No se seleccionó una ubicación para guardar el archivo.")