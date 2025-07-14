# Contenido para: core/auth.py

import streamlit as st

# Por ahora, definimos los usuarios aquí. Más adelante, leeremos las contraseñas
# desde los secretos de Streamlit (st.secrets).
USUARIOS = {
    "gerencia": {"password": "1234", "rol": "GERENTE", "nombre_completo": "Gerencia General"},
    # Agregaremos los demás usuarios (vendedores, tiendas) aquí.
}

def verificar_login(username, password):
    """
    Verifica si el login es correcto y guarda los datos del usuario en la sesión.
    """
    user_data = USUARIOS.get(username.lower())
    
    # Compara la contraseña (por ahora directamente, luego con st.secrets)
    if user_data and user_data["password"] == password:
        # Si es correcto, guardamos la información clave en la sesión
        st.session_state['autenticado'] = True
        st.session_state['rol'] = user_data["rol"]
        st.session_state['nombre_completo'] = user_data["nombre_completo"]
        return True
    
    return False

def tiene_permiso(rol_usuario, modulo_solicitado):
    """
    Verifica si un rol tiene permiso para ver un módulo.
    (Esta función la usaremos más adelante dentro de cada página).
    """
    if rol_usuario == 'GERENTE':
        return True # El gerente puede ver todo
    
    # Aquí definiremos los permisos para los otros roles
    permisos = {
        'VENDEDOR': ['Ventas', 'Cartera', 'Inventarios', 'Cotizaciones'],
        'TIENDA': ['Ventas', 'Cartera', 'Inventarios', 'Cotizaciones']
    }
    
    if modulo_solicitado in permisos.get(rol_usuario, []):
        return True
        
    return False
