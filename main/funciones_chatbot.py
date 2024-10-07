import streamlit as st
from groq import Groq

MODELOS = ['llama3-8b-8192', 'llama3-70b-8192', 'mixtral-8x7b-32768']

def configuracion_inicial():
    modelo_seleccionado = configurar_modelo_usuario()
    return modelo_seleccionado

def inicializar_estado():
    if "mensajes" not in st.session_state:
        st.session_state.mensajes = []

def crear_usuario_groq():
    clave_secreta = st.secrets["CLAVE_API"]
    return Groq(api_key=clave_secreta)

def configurar_modelo_usuario():
    st.sidebar.title("Configuración de la IA")
    elegirModelo = st.sidebar.selectbox('Elegí un Modelo', options=MODELOS, index=0)
    return elegirModelo

def configurar_modelo(cliente, modelo):
    # Crear el contenido de mensajes incluyendo todo el historial
    messages = [{"role": mensaje["role"], "content": mensaje["content"]} for mensaje in st.session_state.mensajes]
    
    respuesta = cliente.chat.completions.create(
        model=modelo,
        messages=messages,
        stream=False
    )
    
    if hasattr(respuesta, 'choices') and len(respuesta.choices) > 0:
        return respuesta.choices[0].message.content
    else:
        return "No se pudo obtener una respuesta del modelo."

def actualizar_historial(rol, contenido, avatar):
    st.session_state.mensajes.append({"role": rol, "content": contenido, "avatar": avatar})

def mostrar_historial():
    if "mensajes" in st.session_state:
        for mensaje in st.session_state.mensajes:
            with st.chat_message(mensaje["role"], avatar=mensaje["avatar"]):
                st.markdown(mensaje["content"])
