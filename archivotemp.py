import pandas as pd
from docx import Document


# Abrir el documento Word existente

horas_planeacion = {
    'Utilizar herramientas informáticas de acuerdo con las necesidades de manejo de información': 48,
    'APLICAR PRÁCTICAS DE PROTECCIÓN AMBIENTAL, SEGURIDAD Y SALUD EN EL TRABAJO DE ACUERDO CON LAS POLÍTICAS ORGANIZACIONALES Y LA NORMATIVIDAD VIGENTE.': 48,
    'Razonar cuantitativamente frente a situaciones susceptibles de ser abordadas de manera matemática en contextos laborales, sociales y personales.': 48,
    'APLICACIÓN DE CONOCIMIENTOS DE LAS CIENCIAS NATURALES DE ACUERDO CON SITUACIONES DEL CONTEXTO PRODUCTIVO Y SOCIAL.': 48,
    'DESARROLLAR PROCESOS DE COMUNICACIÓN EFICACES Y EFECTIVOS, TENIENDO EN CUENTA SITUACIONES  DE ORDEN SOCIAL, PERSONAL Y PRODUCTIVO.': 48,
    'GENERAR HÁBITOS SALUDABLES DE VIDA MEDIANTE LA APLICACIÓN DE PROGRAMAS DE ACTIVIDAD FÍSICA EN LOS CONTEXTOS PRODUCTIVOS Y SOCIALES.': 48,
    'Orientar investigación formativa según referentes técnicos': 48,
    'Enrique Low Murtra-Interactuar en el contexto productivo y social de acuerdo con principios  éticos para la construcción de una cultura de paz.': 48,
    'INTERACTUAR EN LENGUA INGLESA DE FORMA ORAL Y ESCRITA DENTRO DE CONTEXTOS SOCIALES Y LABORALES SEGÚN LOS CRITERIOS ESTABLECIDOS POR EL MARCO COMÚN EUROPEO DE REFERENCIA PARA LAS LENGUAS.': 384 ,
    'Fomentar cultura emprendedora según habilidades y competencias personales': 48
}




# Cargar el archivo de Excel en competencias
dfinstructorhoras = pd.read_excel('Reporte de Instructores por Ficha.xls',header=0,skiprows=10)


dfinstructorhoras['Nombrecompleto'] = dfinstructorhoras['Nombre Instructor'] + ' ' + dfinstructorhoras['Apellido Instructor']
dfinstructorhoras = dfinstructorhoras.sort_values(by='Competencia', ascending=True)

# Añadir la columna 'Horas Planeadas' al DataFrame
dfinstructorhoras['Horas Planeadas'] = dfinstructorhoras['Competencia'].map(horas_planeacion)

dfinstructorhoras = dfinstructorhoras[['Nombrecompleto','Estado Instructor','Competencia','Horas Programadas','Horas Planeadas']]




print(dfinstructorhoras)



#print(dfcompetencias[['Competencia', 'Juicio de Evaluación']])"""


