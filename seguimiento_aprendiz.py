import streamlit as st
import pandas as pd
import numpy as np

def seguimiento_por_aprendiz():
    st.header("Seguimiento por Aprendiz")
    
    # Selector de aprendiz
    aprendices = [f"Aprendiz {i}" for i in range(1, 21)]
    aprendiz_seleccionado = st.selectbox("Seleccione el aprendiz", aprendices)
    
    if aprendiz_seleccionado:
        st.subheader(f"Progreso de {aprendiz_seleccionado}")
        
        # Generar datos de progreso simulados
        competencias = [f"Competencia {i}" for i in range(1, 9)]
        progreso = np.random.randint(0, 100, size=8)
        
        data = {
            'Competencia': competencias,
            'Progreso (%)': progreso,
            'Estado': ['Completada' if x >= 80 else 'En proceso' if x >= 40 else 'Pendiente' for x in progreso]
        }
        
        df = pd.DataFrame(data)
        st.dataframe(df)