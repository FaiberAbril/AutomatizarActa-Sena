import streamlit as st
import pandas as pd
import numpy as np
import os

def seguimiento_a_la_formacion():
    st.header("Seguimiento a la Formación")
    
    # Rutas de los archivos locales
    ruta_programacion = "2849089_PROGRAMACION_2025.xlsx"
    ruta_instructores = "Reporte de Instructores por Ficha.xls"
    
    # Verificar que los archivos existan
    if not os.path.exists(ruta_programacion):
        st.error(f"Archivo no encontrado: {ruta_programacion}")
        return
    
    if not os.path.exists(ruta_instructores):
        st.error(f"Archivo no encontrado: {ruta_instructores}")
        return
    
    try:
        # Cargar los archivos de Excel locales
        df_excel = pd.read_excel(ruta_programacion, header=0, skiprows=1)
        df_instructores = pd.read_excel(ruta_instructores, header=0, skiprows=10)
        
        # Función para sumar las horas programadas por competencia
        def sumar_horas_por_competencia(df):
            horas_por_competencia = df.groupby('Competencia', as_index=False)['Horas Programadas'].sum()
            return horas_por_competencia
        
        # Función para sumar horas totales
        def sumar_horas_totales(df):
            # Verificar si la columna existe (puede tener espacio al final)
            if 'Total ' in df.columns:
                suma_total = df['Total '].sum()
            elif 'Total' in df.columns:
                suma_total = df['Total'].sum()
            else:
                st.warning("Columna 'Total' no encontrada en el archivo de programación")
                suma_total = 0
            return suma_total
        
        # Función para sumar horas ejecutadas
        def sumar_horas_ejecutadas(df):
            if 'Ejecutadas' in df.columns:
                suma_total = df['Ejecutadas'].sum()
            else:
                st.warning("Columna 'Ejecutadas' no encontrada en el archivo de programación")
                suma_total = 0
            return suma_total
        
        # Obtener los datos
        horas_por_competencia = sumar_horas_por_competencia(df_instructores)
        horas_totales = sumar_horas_totales(df_excel)
        horas_ejecutadas = sumar_horas_ejecutadas(df_excel)
        
        # Mostrar estadísticas
        st.subheader("Estadísticas de Horas")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Horas Totales del Programa", f"{horas_totales:,.0f}")
        
        with col2:
            st.metric("Horas Ejecutadas", f"{horas_ejecutadas:,.0f}")
        
        with col3:
            porcentaje_ejecucion = (horas_ejecutadas / horas_totales * 100) if horas_totales > 0 else 0
            st.metric("% de Ejecución", f"{porcentaje_ejecucion:.1f}%")
        
        # Mostrar horas por competencia
        st.subheader("Horas Programadas por Competencia")
        st.dataframe(horas_por_competencia, use_container_width=True, height=600)
        
        
                
    except Exception as e:
        st.error(f"Error al procesar los archivos: {str(e)}")
        st.info("Asegúrate de que los archivos tengan la estructura correcta:")
        st.write("- Archivo de Programación: Debe tener columnas 'Total ' y 'Ejecutadas'")
        st.write("- Reporte de Instructores: Debe tener columnas 'Competencia' y 'Horas Programadas'")

# Si se ejecuta este archivo directamente
if __name__ == "__main__":
    seguimiento_a_la_formacion()