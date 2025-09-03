import streamlit as st
import pandas as pd
import numpy as np

def acta_por_competencia():
    st.header("Acta por Competencia")
    
    competencia = st.selectbox("Seleccione la competencia", 
                             ["Programación básica", "Bases de datos", 
                              "Desarrollo web", "Análisis de datos"])
    
    if competencia:
        st.subheader(f"Resultados para {competencia}")
        
        # Generar datos de ejemplo
        aprendices = [f"Aprendiz {i}" for i in range(1, 11)]
        calificaciones = np.random.randint(0, 100, size=10)
        
        data = {
            'Aprendiz': aprendices,
            'Calificación': calificaciones,
            'Estado': ['Aprobado' if x >= 70 else 'Reprobado' for x in calificaciones]
        }
        
        df = pd.DataFrame(data)
        st.dataframe(df)