# Dentro de main.py

import streamlit as st
from core.auth import verificar_login, tiene_permiso # Importamos desde nuestro nuevo gestor
from core.data_manager import get_all_data # Importamos el gestor de datos

# --- 1. Configuración Inicial de la Página ---
st.set_page_config(
    page_title="Plataforma Ferreinox",
    page_icon="https://raw.githubusercontent.com/DiegoMao201/Resumen-Ventas-Gerenciales/main/LOGO%20FERREINOX%20SAS%20BIC%202024.png", # Puedes usar una URL para el ícono
    layout="centered" # Usamos un layout centrado para el login
)

# --- 2. Lógica de la Pantalla de Login ---

# Verificamos si el usuario ya está autenticado en la sesión
if not st.session_state.get('autenticado', False):
    
    st.image("https://raw.githubusercontent.com/DiegoMao201/Resumen-Ventas-Gerenciales/main/LOGO%20FERREINOX%20SAS%20BIC%202024.png", width=300)
    st.title("Plataforma de Inteligencia de Negocios")
    st.header("Inicio de Sesión")

    # Creamos el formulario de login
    with st.form("login_form"):
        username = st.text_input("Usuario")
        password = st.text_input("Contraseña", type="password")
        submitted = st.form_submit_button("Ingresar")

        if submitted:
            # Llamamos a nuestra función de verificación del core/auth.py
            # Esta función devolverá True si el login es exitoso
            if verificar_login(username, password):
                st.session_state['autenticado'] = True
                # Forzamos a Streamlit a recargar la página.
                # Al recargar, la condición de arriba será False y mostrará el contenido principal.
                st.rerun()
            else:
                st.error("Usuario o contraseña incorrectos.")

# --- 3. Lógica Principal de la Aplicación (Post-Login) ---
else:
    # --- ESTE CÓDIGO SOLO SE EJECUTA SI EL USUARIO ESTÁ AUTENTICADO ---

    # Cambiamos el layout a ancho para los dashboards
    st.set_page_config(layout="wide") 

    # Saludamos al usuario. El nombre completo se guardó en la sesión durante el login.
    st.sidebar.title(f"Bienvenido(a), {st.session_state.get('nombre_completo', '')}")
    st.sidebar.markdown("---")
    
    # Mensaje de bienvenida en la página principal
    st.header("Bienvenido a la Plataforma de Inteligencia de Negocios Ferreinox")
    st.info("Utilice el menú de la izquierda para navegar entre los diferentes módulos.")

    # Con un botón, permitimos cerrar la sesión de forma segura
    if st.sidebar.button("Cerrar Sesión"):
        # Limpiamos todas las variables de la sesión para un logout completo
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        # Recargamos la página para volver a la pantalla de login
        st.rerun()
        
    # --- Precarga de Datos (Opcional pero Recomendado) ---
    # Podemos hacer que la primera vez que un usuario inicia sesión,
    # se carguen todos los datos en segundo plano.
    if 'data' not in st.session_state:
        with st.spinner("Cargando datos maestros, por favor espere un momento..."):
            # Llamamos a nuestra función maestra del data_manager
            st.session_state['data'] = get_all_data()
        st.toast("¡Datos cargados exitosamente!", icon="✅")


