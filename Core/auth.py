# Dentro de core/auth.py

import streamlit as st

# 1. Definimos los grupos de tiendas como nos indicaste.
# Esta estructura nos permitirá asignar un vendedor a una tienda.
GRUPOS_TIENDAS = {
    "TIENDA_ARMENIA": ["CRISTIAN CAMILO RENDON MONTES", "FANDRY JOHANA ABRIL PENHA", "JAVIER ORLANDO PATINO HURTADO"],
    "TIENDA_MANIZALES": ["DAVID FELIPE MARTINEZ RIOS", "JHON JAIRO CASTAÑO MONTES"],
    # ...y los demás grupos que definiste en tu app de ventas.
}

# 2. Definimos los roles y usuarios. Las contraseñas se leerán desde st.secrets.
# El rol 'TIENDA' es especial y se le asignará a los vendedores que pertenezcan a un grupo.
USUARIOS = {
    "gerencia": {"rol": "GERENTE", "nombre_completo": "Gerencia General"},
    "vendedor_alejandro": {"rol": "VENDEDOR", "nombre_completo": "ALEJANDRO CARBALLO MARQUEZ"},
    "tienda_armenia": {"rol": "TIENDA", "nombre_completo": "Tienda Armenia", "miembros": GRUPOS_TIENDAS["TIENDA_ARMENIA"]},
    # ...y así para cada usuario y tienda.
}

def verificar_login(username, password):
    """Verifica si el usuario y contraseña son correctos y guarda el rol en la sesión."""
    # Lógica para comparar con st.secrets y guardar en st.session_state
    pass

def tiene_permiso(rol_usuario, modulo_solicitado):
    """Verifica si un rol tiene acceso a un módulo específico."""
    if rol_usuario == 'GERENTE':
        return True # El gerente tiene acceso a todo.
    
    permisos = {
        'VENDEDOR': ['Ventas', 'Cartera', 'Inventarios', 'Cotizaciones', 'Formulario'],
        'TIENDA': ['Ventas', 'Cartera', 'Inventarios', 'Cotizaciones', 'Formulario'],
        # Podemos añadir más roles si es necesario
    }
    
    if modulo_solicitado in permisos.get(rol_usuario, []):
        return True
    return False

def obtener_vendedores_para_filtrar(rol_usuario, nombre_usuario_completo):
    """Devuelve la lista de nombres de vendedores que se deben usar para filtrar los datos."""
    if rol_usuario == 'GERENTE':
        return "TODOS" # Una señal para no filtrar
    elif rol_usuario == 'TIENDA':
        # Devuelve la lista de miembros de esa tienda
        for tienda in GRUPOS_TIENDAS.values():
            if nombre_usuario_completo in tienda:
                 return tienda
        return [nombre_usuario_completo] # Fallback por si acaso
    else: # Es un VENDEDOR individual
        return [nombre_usuario_completo]

