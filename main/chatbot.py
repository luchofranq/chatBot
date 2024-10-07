import streamlit as st
import funciones_chatbot as fc

def main():
    # Configurar la página
    st.set_page_config(page_title="Mi chat de IA", page_icon="♦", layout="centered")

  
    
    # Tema oscuro/claro
    if 'tema' not in st.session_state:
        st.session_state.tema = 'light'  # Tema predeterminado

   

    modelo = fc.configuracion_inicial()  # Inicializar configuración del modelo
    fc.inicializar_estado()  # Inicializar estado

    mensaje_usuario = st.chat_input("Escribí tu mensaje:")  # Input del usuario

    if mensaje_usuario:
        clienteUsuario = fc.crear_usuario_groq()  # Crear el cliente Groq
        fc.actualizar_historial("user", mensaje_usuario, "🙂")  # Actualizar historial

        respuesta_asistente = fc.configurar_modelo(clienteUsuario, modelo)  # Obtener respuesta del asistente
        fc.actualizar_historial("assistant", respuesta_asistente, "🤖")  # Actualizar historial con respuesta

    # Mostrar el historial en la interfaz
    fc.mostrar_historial()

# Ejecutar la función principal
if __name__ == "__main__":
    main()
