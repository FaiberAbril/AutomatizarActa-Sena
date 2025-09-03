import streamlit as st
import random
import string
import secrets
import pyperclip

def generar_contrasena():
    st.title("🔐 Generador de Contraseñas Seguras")
    
    st.markdown("---")
    
    # Configuración de la contraseña
    col1, col2 = st.columns(2)
    
    with col1:
        longitud = st.slider("Longitud de la contraseña", 
                        min_value=8, 
                        max_value=32, 
                        value=12,
                        help="Recomendado: 12-16 caracteres")
    
    with col2:
        num_contrasenas = st.slider("Número de contraseñas a generar", 
                                min_value=1, 
                                max_value=10, 
                                value=3)
    
    # Opciones de caracteres
    st.subheader("🔧 Opciones de caracteres")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        usar_mayusculas = st.checkbox("Mayúsculas (A-Z)", value=True)
    with col2:
        usar_minusculas = st.checkbox("Minúsculas (a-z)", value=True)
    with col3:
        usar_numeros = st.checkbox("Números (0-9)", value=True)
    with col4:
        usar_especiales = st.checkbox("Símbolos (@#$%)", value=True)
    
    # Caracteres personalizados
    caracteres_personalizados = st.text_input("Caracteres personalizados (opcional)", 
                                            placeholder="!*-+=",
                                            help="Agrega símbolos específicos que quieras incluir")
    
    # Botón para generar
    if st.button("🎯 Generar Contraseñas", type="primary"):
        if not any([usar_mayusculas, usar_minusculas, usar_numeros, usar_especiales]) and not caracteres_personalizados:
            st.error("⚠️ Debes seleccionar al menos un tipo de carácter")
            return
        
        contrasenas = []
        for _ in range(num_contrasenas):
            contrasena = generar_contrasena_segura(
                longitud=longitud,
                mayusculas=usar_mayusculas,
                minusculas=usar_minusculas,
                numeros=usar_numeros,
                especiales=usar_especiales,
                personalizados=caracteres_personalizados
            )
            contrasenas.append(contrasena)
        
        # Mostrar resultados
        st.success("✅ Contraseñas generadas con éxito!")
        st.markdown("---")
        
        for i, contrasena in enumerate(contrasenas, 1):
            col1, col2 = st.columns([3, 1])
            with col1:
                st.code(contrasena, language="text")
            with col2:
                st.button("📋 Copiar", key=f"copy_{i}", 
                            on_click=copiar_al_portapapeles, 
                            args=(contrasena,),
                            use_container_width=True)
        
      
       

def generar_contrasena_segura(longitud=12, mayusculas=True, minusculas=True, 
                            numeros=True, especiales=True, personalizados=""):
    """Genera una contraseña segura usando secrets"""
    caracteres = ""
    
    if mayusculas:
        caracteres += string.ascii_uppercase
    if minusculas:
        caracteres += string.ascii_lowercase
    if numeros:
        caracteres += string.digits
    if especiales:
        caracteres += string.punctuation
    if personalizados:
        caracteres += personalizados
    
    if not caracteres:
        caracteres = string.ascii_letters + string.digits
    
    # Asegurar que haya al menos un carácter de cada tipo seleccionado
    contrasena = []
    
    if mayusculas:
        contrasena.append(secrets.choice(string.ascii_uppercase))
    if minusculas:
        contrasena.append(secrets.choice(string.ascii_lowercase))
    if numeros:
        contrasena.append(secrets.choice(string.digits))
    if especiales and string.punctuation:
        contrasena.append(secrets.choice(string.punctuation))
    if personalizados:
        contrasena.append(secrets.choice(personalizados))
    
    # Completar el resto de la contraseña
    contrasena.extend(secrets.choice(caracteres) for _ in range(longitud - len(contrasena)))
    
    # Mezclar la contraseña
    secrets.SystemRandom().shuffle(contrasena)
    
    return ''.join(contrasena)

def copiar_al_portapapeles(texto):
    """Copia texto al portapapeles"""
    
    try:
        pyperclip.copy(texto)
        st.toast("📋 Contraseña copiada al portapapeles!")
    except:
        # Fallback para entornos sin pyperclip
        st.warning("No se pudo copiar automáticamente. Selecciona y copia manualmente.")


# Ejecutar la aplicación
if __name__ == "__main__":
    generar_contrasena()