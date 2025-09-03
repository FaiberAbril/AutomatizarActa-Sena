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
                        
                        st.subheader("3. Tipo de reporte")
                        
                        # Checkboxes para seleccionar el tipo de reporte
                        col1, col2 = st.columns(2)
                        
                        with col1:
                            reporte_completo = st.checkbox("Reporte completo de la competencia", value=True)
                        
                        with col2:
                            if 'Resultado de Aprendizaje' in df_competencia.columns:
                                reporte_detallado = st.checkbox("Reporte por resultados de aprendizaje")
                            else:
                                reporte_detallado = st.checkbox("Reporte por resultados de aprendizaje", disabled=True)
                                st.caption("Columna 'Resultado de Aprendizaje' no encontrada")
                        
                        if reporte_completo:
                            st.subheader(f"4. Listado Completo - {competencia_seleccionada}")
                            
                            # Crear tabla resumen de aprendices para la competencia completa
                            if 'Nombre completo' in df_competencia.columns and 'Juicio de Evaluación' in df_competencia.columns:
                                # Obtener datos únicos por aprendiz
                                aprendices_data = df_competencia[['Nombre completo', 'Número de Documento', 'Estado', 'Juicio de Evaluación']].drop_duplicates(subset=['Nombre completo'])
                                
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
                                
                                # Mostrar tabla completa de aprendices
                                st.dataframe(aprendices_data, use_container_width=True, height=400)
                                
                                # Opción para descargar el reporte completo
                                csv_completo = aprendices_data.to_csv(index=False)
                                st.download_button(
                                    label="📥 Descargar reporte completo",
                                    data=csv_completo,
                                    file_name=f"reporte_completo_{competencia_seleccionada.replace(' ', '_')}.csv",
                                    mime="text/csv"
                                )
                        
                        if reporte_detallado and 'Resultado de Aprendizaje' in df_competencia.columns:
                            st.subheader(f"5. Reporte por Resultados de Aprendizaje - {competencia_seleccionada}")
                            
                            # Obtener lista única de resultados de aprendizaje
                            resultados_aprendizaje = df_competencia['Resultado de Aprendizaje'].unique().tolist()
                            resultados_aprendizaje.sort()
                            
                            resultado_seleccionado = st.selectbox("Seleccione el resultado de aprendizaje", resultados_aprendizaje)
                            
                            if resultado_seleccionado:
                                # Filtrar por resultado de aprendizaje específico
                                df_resultado = df_competencia[df_competencia['Resultado de Aprendizaje'] == resultado_seleccionado]
                                
                                # Obtener datos únicos por aprendiz para este resultado
                                aprendices_resultado = df_resultado[['Nombre completo', 'Número de Documento', 'Estado', 'Juicio de Evaluación']].drop_duplicates(subset=['Nombre completo'])
                                
                                # Mostrar estadísticas del resultado específico
                                st.subheader(f"Estadísticas - {resultado_seleccionado}")
                                
                                total_aprendices_resultado = len(aprendices_resultado)
                                aprobados_resultado = len(aprendices_resultado[aprendices_resultado['Juicio de Evaluación'] == 'APROBADO'])
                                
                                col1, col2, col3 = st.columns(3)
                                
                                with col1:
                                    st.metric("Total Aprendices", total_aprendices_resultado)
                                
                                with col2:
                                    st.metric("Aprobados", aprobados_resultado)
                                
                                with col3:
                                    if total_aprendices_resultado > 0:
                                        porcentaje_aprobacion_resultado = (aprobados_resultado / total_aprendices_resultado * 100)
                                        st.metric("% Aprobación", f"{porcentaje_aprobacion_resultado:.1f}%")
                                
                                # Mostrar tabla de aprendices para este resultado
                                st.dataframe(aprendices_resultado, use_container_width=True, height=300)
                                
                                # Opción para descargar el reporte detallado
                                csv_detallado = aprendices_resultado.to_csv(index=False)
                                st.download_button(
                                    label=f"📥 Descargar reporte - {resultado_seleccionado[:30]}...",
                                    data=csv_detallado,
                                    file_name=f"reporte_{resultado_seleccionado.replace(' ', '_')[:20]}.csv",
                                    mime="text/csv"
                                )
                        
                        if not reporte_completo and not reporte_detallado:
                            st.info("Seleccione al menos un tipo de reporte para continuar")

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