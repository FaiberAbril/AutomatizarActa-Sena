import streamlit as st
import pandas as pd
import numpy as np

def seguimiento_por_aprendiz():
    st.header("Seguimiento por Aprendiz")
    
    # Cargar archivo
    st.subheader("1. Cargar archivo de juicios evaluativos")
    
    archivo_juicios = st.file_uploader("Seleccione el archivo Excel de juicios evaluativos", 
                                    type=['xls', 'xlsx'],
                                    key="juicios_aprendiz")
    
    if archivo_juicios:
        try:
            # Cargar el archivo de Excel
            df = pd.read_excel(archivo_juicios, header=0, skiprows=12)
            
            # Crear columna de nombre completo
            if 'Nombre' in df.columns and 'Apellidos' in df.columns:
                df['Nombre completo'] = df['Nombre'] + ' ' + df['Apellidos']
                
                # Obtener lista única de aprendices
                aprendices = df['Nombre completo'].unique().tolist()
                aprendices.sort()  # Ordenar alfabéticamente
                
                if not aprendices:
                    st.warning("No se encontraron aprendices en el archivo")
                    return
                
                st.subheader("2. Seleccionar aprendiz")
                # Selector de aprendiz
                aprendiz_seleccionado = st.selectbox("Seleccione el aprendiz", aprendices)
                
                if aprendiz_seleccionado:
                    st.subheader(f"Progreso de {aprendiz_seleccionado}")
                    
                    # Filtrar datos del aprendiz seleccionado
                    datos_aprendiz = df[df['Nombre completo'] == aprendiz_seleccionado]
                    
                    if not datos_aprendiz.empty:
                        # Mostrar información básica del aprendiz
                        col1, col2, col3 = st.columns(3)
                        
                        with col1:
                            documento = datos_aprendiz['Número de Documento'].iloc[0] if 'Número de Documento' in datos_aprendiz.columns else "N/A"
                            st.metric("Documento", documento)
                        
                        with col2:
                            estado = datos_aprendiz['Estado'].iloc[0] if 'Estado' in datos_aprendiz.columns else "N/A"
                            st.metric("Estado", estado)
                        
                        with col3:
                            ficha = datos_aprendiz['Ficha'].iloc[0] if 'Ficha' in datos_aprendiz.columns else "N/A"
                            st.metric("Ficha", ficha)
                        
                        # Mostrar competencias y juicios de evaluación
                        st.subheader("Competencias y Evaluaciones")
                        
                        if 'Competencia' in datos_aprendiz.columns and 'Juicio de Evaluación' in datos_aprendiz.columns:
                            competencias_data = datos_aprendiz[['Competencia', 'Juicio de Evaluación']].drop_duplicates()
                            st.dataframe(competencias_data)
                            
                            # Calcular estadísticas
                            aprobadas = len(competencias_data[competencias_data['Juicio de Evaluación'] == 'APROBADO'])
                            total_competencias = len(competencias_data)
                            porcentaje_aprobacion = (aprobadas / total_competencias * 100) if total_competencias > 0 else 0
                            
                            col1, col2, col3 = st.columns(3)
                            col1.metric("Competencias totales", total_competencias)
                            col2.metric("Competencias aprobadas", aprobadas)
                            col3.metric("% de aprobación", f"{porcentaje_aprobacion:.1f}%")
                        
                        # Mostrar todos los datos del aprendiz
                        with st.expander("Ver todos los datos del aprendiz"):
                            st.dataframe(datos_aprendiz)
                    
                    else:
                        st.warning("No se encontraron datos para el aprendiz seleccionado")
            
            else:
                st.error("El archivo no contiene las columnas 'Nombre' y 'Apellidos' necesarias")
                st.info("Columnas encontradas en el archivo:")
                st.write(list(df.columns))
                
        except Exception as e:
            st.error(f"Error al procesar el archivo: {str(e)}")
    
    else:
        st.info("Por favor, cargue el archivo de juicios evaluativos para continuar")

# Si se ejecuta este archivo directamente
if __name__ == "__main__":
    seguimiento_por_aprendiz()