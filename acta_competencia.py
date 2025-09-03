import streamlit as st
import pandas as pd
import numpy as np

def acta_por_competencia():
    st.header("Acta por Competencia")
    
    # Cargar archivo
    st.subheader("1. Cargar archivo de juicios evaluativos")
    
    archivo_juicios = st.file_uploader("Seleccione el archivo Excel de juicios evaluativos", 
                                    type=['xls', 'xlsx'],
                                    key="juicios_competencia")
    
    if archivo_juicios:
        try:
            # Cargar el archivo de Excel
            df = pd.read_excel(archivo_juicios, header=0, skiprows=12)
            
            # Crear columna de nombre completo
            if 'Nombre' in df.columns and 'Apellidos' in df.columns:
                df['Nombre completo'] = df['Nombre'] + ' ' + df['Apellidos']
                
                # Obtener lista única de competencias
                if 'Competencia' in df.columns:
                    competencias = df['Competencia'].unique().tolist()
                    competencias.sort()  # Ordenar alfabéticamente
                    
                    if not competencias:
                        st.warning("No se encontraron competencias en el archivo")
                        return
                    
                    st.subheader("2. Seleccionar competencia")
                    # Selector de competencia
                    competencia_seleccionada = st.selectbox("Seleccione la competencia", competencias)
                    
                    if competencia_seleccionada:
                        # Filtrar datos por la competencia seleccionada
                        df_competencia = df[df['Competencia'] == competencia_seleccionada]
                        
                        st.subheader(f"3. Listado de Aprendices - {competencia_seleccionada}")
                        
                        # Crear tabla resumen de aprendices
                        if 'Nombre completo' in df_competencia.columns and 'Juicio de Evaluación' in df_competencia.columns:
                            # Obtener datos únicos por aprendiz
                            aprendices_data = df_competencia[['Nombre completo', 'Número de Documento', 'Estado', 'Juicio de Evaluación']].drop_duplicates(subset=['Nombre completo'])
                            
                            # Mostrar tabla completa de aprendices
                            st.dataframe(aprendices_data, use_container_width=True)
                            
                            # Mostrar estadísticas
                            st.subheader("Estadísticas de la Competencia")
                            
                            total_aprendices = len(aprendices_data)
                            aprobados = len(aprendices_data[aprendices_data['Juicio de Evaluación'] == 'APROBADO'])
                            por_evaluar = len(aprendices_data[aprendices_data['Juicio de Evaluación'] == 'POR EVALUAR'])
                            
                            col1, col2, col3, col4 = st.columns(4)
                            
                            with col1:
                                st.metric("Total Aprendices", total_aprendices)
                            
                            with col2:
                                st.metric("Aprobados", aprobados)
                            
                            with col3:
                                st.metric("Por Evaluar", por_evaluar)
                            
                            with col4:
                                if total_aprendices > 0:
                                    porcentaje_aprobacion = (aprobados / total_aprendices * 100)
                                    st.metric("% Aprobación", f"{porcentaje_aprobacion:.1f}%")
                            
                            # Gráfico de estado de evaluación
                            st.subheader("Distribución de Juicios de Evaluación")
                            
                            if total_aprendices > 0:
                                # Crear datos para el gráfico
                                estados = aprendices_data['Juicio de Evaluación'].value_counts()
                                st.bar_chart(estados)
                            
                            # Opción para descargar el reporte
                            st.subheader("4. Exportar Reporte")
                            
                            # Convertir DataFrame a CSV
                            csv = aprendices_data.to_csv(index=False)
                            st.download_button(
                                label="📥 Descargar reporte en CSV",
                                data=csv,
                                file_name=f"reporte_competencia_{competencia_seleccionada.replace(' ', '_')}.csv",
                                mime="text/csv"
                            )
                            
                        else:
                            st.error("El archivo no contiene las columnas necesarias para generar el reporte")
                            st.info("Columnas necesarias: 'Nombre completo', 'Juicio de Evaluación'")
                
                else:
                    st.error("El archivo no contiene la columna 'Competencia'")
                    st.info("Columnas encontradas en el archivo:")
                    st.write(list(df.columns))
            
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
    acta_por_competencia()