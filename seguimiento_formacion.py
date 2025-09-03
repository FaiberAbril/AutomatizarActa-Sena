import streamlit as st
import pandas as pd
import numpy as np

def seguimiento_a_la_formacion():
    st.header("Seguimiento a la Formación")
    
    # Selector de programa
    programas = ["Técnico en Programación", "Técnico en Sistemas", "Técnico en Redes", "Analista de Datos"]
    programa_seleccionado = st.selectbox("Seleccione el programa", programas)
    
    if programa_seleccionado:
        st.subheader(f"Estadísticas de {programa_seleccionado}")
        
        # Generar datos simulados
        meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun"]
        matriculados = np.random.randint(50, 100, size=6)
        aprobados = [int(x * np.random.uniform(0.7, 0.9)) for x in matriculados]
        
        data = {
            'Mes': meses,
            'Matriculados': matriculados,
            'Aprobados': aprobados,
            'Tasa de aprobación': [f"{(a/m)*100:.1f}%" for a, m in zip(aprobados, matriculados)]
        }
        
        df = pd.DataFrame(data)
        st.dataframe(df)