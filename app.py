import streamlit as st
import pandas as pd
import numpy as np

# Importar las funciones de los módulos
from acta_trimestral import acta_trimestral
from acta_competencia import acta_por_competencia
from seguimiento_aprendiz import seguimiento_por_aprendiz
from seguimiento_formacion import seguimiento_a_la_formacion


# Configuración de la página
st.set_page_config(
    page_title="Sistema de Seguimiento de Formación",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título principal
st.title("Sistema de Seguimiento de Formación")
st.markdown("---")

# Crear navegación en la barra lateral
st.sidebar.title("Navegación")
opcion = st.sidebar.radio(
    "Seleccione una opción:",
    ["Inicio", "Acta Trimestral", "Acta por Competencia", "Seguimiento por Aprendiz", "Seguimiento a la Formación"]
)

# Mostrar la sección correspondiente
if opcion == "Inicio":
    st.header("Bienvenido al Sistema de Seguimiento de Formación")
    st.markdown("""
    Esta aplicación le permite generar reportes y realizar seguimiento a:
    - Actas trimestrales de formación
    - Actas por competencia específica
    - Seguimiento individual por aprendiz
    - Seguimiento general de la formación
    
    Utilice el menú de la izquierda para navegar entre las diferentes secciones.
    """)
    
    # Mostrar estadísticas rápidas en la página de inicio
    st.subheader("Resumen Estadístico")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Aprendices", "243")
    col2.metric("Tasa de Aprobación", "87%")
    col3.metric("Programas Activos", "4")
    col4.metric("Competencias Evaluadas", "32")
    
elif opcion == "Acta Trimestral":
    acta_trimestral()
    
elif opcion == "Acta por Competencia":
    acta_por_competencia()
    
elif opcion == "Seguimiento por Aprendiz":
    seguimiento_por_aprendiz()
    
elif opcion == "Seguimiento a la Formación":
    seguimiento_a_la_formacion()

# Pie de página
st.markdown("---")
st.markdown("Sistema de Seguimiento de Formación © 2023 - Desarrollado con Streamlit")