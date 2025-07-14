# Contenido para: core/data_manager.py

import streamlit as st
import pandas as pd

@st.cache_data
def get_all_data():
    """
    Esta será la función maestra que cargará todos los datos.
    Por ahora, devuelve un diccionario vacío para que la app no se rompa.
    """
    # Más adelante, aquí irá toda la lógica de carga de Dropbox y G-Sheets.
    print("El gestor de datos fue llamado, pero aún no carga datos.")
    
    data = {
        "cartera": pd.DataFrame(),
        "ventas": pd.DataFrame(),
        "inventario": pd.DataFrame(),
        "maestros": pd.DataFrame()
    }
    return data
