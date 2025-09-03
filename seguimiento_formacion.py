import streamlit as st
import pandas as pd
import numpy as np
import os
import tempfile

def seguimiento_a_la_formacion():
    st.header("Seguimiento a la Formación")
    
    # Solicitar archivos mediante la interfaz
    st.subheader("1. Cargar archivos requeridos")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Archivo de Programación**")
        archivo_programacion = st.file_uploader("Seleccione el archivo Excel de programación", 
                                              type=['xlsx', 'xls'],
                                              key="programacion",
                                              help="Archivo con las horas totales y ejecutadas")
    
    with col2:
        st.markdown("**Reporte de Instructores por Ficha**")
        archivo_instructores = st.file_uploader("Seleccione el archivo de instructores", 
                                              type=['xls', 'xlsx'],
                                              key="instructores",
                                              help="Archivo con las horas programadas por competencia")
    
    # Verificar que ambos archivos estén cargados
    if archivo_programacion is not None and archivo_instructores is not None:
        try:
            # Guardar archivos temporalmente
            with tempfile.TemporaryDirectory() as temp_dir:
                # Guardar archivo de programación
                ruta_programacion = os.path.join(temp_dir, "programacion.xlsx")
                with open(ruta_programacion, "wb") as f:
                    f.write(archivo_programacion.getbuffer())
                
                # Guardar archivo de instructores
                ruta_instructores = os.path.join(temp_dir, "instructores.xls")
                with open(ruta_instructores, "wb") as f:
                    f.write(archivo_instructores.getbuffer())
                
                # Cargar los archivos de Excel
                df_excel = pd.read_excel(ruta_programacion, header=0, skiprows=1)
                df_instructores = pd.read_excel(ruta_instructores, header=0, skiprows=10)
                
                # Mostrar información de los archivos cargados
                st.success("✅ Archivos cargados correctamente")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.info(f"**Archivo de programación:** {archivo_programacion.name}")
                    
                
                with col2:
                    st.info(f"**Archivo de instructores:** {archivo_instructores.name}")
                   
                
                # Función para sumar las horas programadas por competencia
                def sumar_horas_por_competencia(df):
                    if 'Competencia' in df.columns and 'Horas Programadas' in df.columns:
                        horas_por_competencia = df.groupby('Competencia', as_index=False)['Horas Programadas'].sum()
                        return horas_por_competencia
                    else:
                        st.error("El archivo de instructores no tiene las columnas esperadas: 'Competencia' y 'Horas Programadas'")
                        return pd.DataFrame()
                
                # Función para sumar horas totales
                def sumar_horas_totales(df):
                    # Verificar si la columna existe (puede tener espacio al final)
                    if 'Total ' in df.columns:
                        suma_total = df['Total '].sum()
                    elif 'Total' in df.columns:
                        suma_total = df['Total'].sum()
                    else:
                        st.error("Columna 'Total' no encontrada en el archivo de programación")
                        # Mostrar columnas disponibles para debug
                        st.write("Columnas disponibles en archivo de programación:")
                        st.write(list(df.columns))
                        suma_total = 0
                    return suma_total
                
                # Función para sumar horas ejecutadas
                def sumar_horas_ejecutadas(df):
                    if 'Ejecutadas' in df.columns:
                        suma_total = df['Ejecutadas'].sum()
                    else:
                        st.error("Columna 'Ejecutadas' no encontrada en el archivo de programación")
                        # Mostrar columnas disponibles para debug
                        st.write("Columnas disponibles en archivo de programación:")
                        st.write(list(df.columns))
                        suma_total = 0
                    return suma_total
                
                # Obtener los datos
                horas_por_competencia = sumar_horas_por_competencia(df_instructores)
                horas_totales = sumar_horas_totales(df_excel)
                horas_ejecutadas = sumar_horas_ejecutadas(df_excel)
                
                # Mostrar estadísticas solo si se obtuvieron datos válidos
                if horas_totales > 0 and not horas_por_competencia.empty:
                    st.subheader("📊 Estadísticas de Horas")
                    
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        st.metric("Horas Totales del Programa", f"{horas_totales:,.0f}")
                    
                    with col2:
                        st.metric("Horas Ejecutadas", f"{horas_ejecutadas:,.0f}")
                    
                    with col3:
                        porcentaje_ejecucion = (horas_ejecutadas / horas_totales * 100) if horas_totales > 0 else 0
                        st.metric("% de Ejecución", f"{porcentaje_ejecucion:.1f}%")
                    
                    # Mostrar horas por competencia
                    st.subheader("📋 Horas Programadas por Competencia")
                    st.dataframe(horas_por_competencia, use_container_width=True, height=400)
                    
                                
        except Exception as e:
            st.error(f"❌ Error al procesar los archivos: {str(e)}")
            st.info("ℹ️ Asegúrate de que los archivos tengan la estructura correcta:")
            st.write("- Archivo de Programación: Debe tener columnas 'Total' y 'Ejecutadas'")
            st.write("- Reporte de Instructores: Debe tener columnas 'Competencia' y 'Horas Programadas'")
    
    else:
        st.warning("⚠️ Por favor, carga ambos archivos para continuar")
        st.info("ℹ️ Necesitas cargar:")
        st.write("1. **Archivo de Programación** (con horas totales y ejecutadas)")
        st.write("2. **Reporte de Instructores por Ficha** (con horas por competencia)")

# Si se ejecuta este archivo directamente
if __name__ == "__main__":
    seguimiento_a_la_formacion()